#!/usr/bin/env python3
"""Generate an image with RefCamera role-separated A/B references.

The helper is deliberately small and dependency-free. It uses existing local
environment variables or ~/.codex/secrets/media-tools.env; it never prints keys.
"""

import argparse
import base64
import json
import mimetypes
import os
from pathlib import Path
import sys
import urllib.error
import urllib.parse
import urllib.request


DEFAULT_ENV_FILES = (
    Path.home() / ".codex/secrets/media-tools.env",
    Path.home() / ".dsh/secrets/media-tools.env",
)


def load_key(name: str) -> str:
    value = os.environ.get(name)
    if value:
        return value.strip()
    for env_path in DEFAULT_ENV_FILES:
        if env_path.exists():
            for line in env_path.read_text().splitlines():
                if line.startswith(name + "="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit(f"missing {name}; set it or configure ~/.codex/secrets/media-tools.env")


def is_url(value: str) -> bool:
    return urllib.parse.urlparse(value).scheme in ("http", "https")


def image_to_data_url(value: str) -> str:
    if value.startswith("data:image/"):
        return value
    if is_url(value):
        request = urllib.request.Request(value, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=90) as response:
            data = response.read()
            content_type = response.headers.get_content_type()
    else:
        path = Path(value).expanduser().resolve()
        data = path.read_bytes()
        content_type = mimetypes.guess_type(str(path))[0] or "image/jpeg"
    return f"data:{content_type};base64," + base64.b64encode(data).decode("ascii")


def post_json(url: str, headers: dict, body: dict, timeout: int):
    request = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json", **headers},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.load(response)


def download_url(url: str, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(url, output)


def extract_image_url(data: dict) -> str:
    images = data.get("images")
    if isinstance(images, list) and images:
        item = images[0]
        if isinstance(item, str):
            return item
        if isinstance(item, dict):
            return item.get("url") or item.get("image_url") or ""
    items = data.get("data")
    if isinstance(items, list) and items:
        item = items[0]
        if isinstance(item, str):
            return item
        if isinstance(item, dict):
            return item.get("url") or item.get("image_url") or ""
    return ""


def generate_siliconflow_qwen_edit(args) -> Path:
    key = load_key("SILICONFLOW_API_KEY")
    url = "https://api.siliconflow.cn/v1/images/generations"
    headers = {"Authorization": "Bearer " + key, "X-Enable-Watermark": "0"}
    base_body = {
        "model": args.model or "Qwen/Qwen-Image-Edit-2509",
        "prompt": args.prompt,
        "negative_prompt": args.negative_prompt,
        "batch_size": 1,
        "image": args.image_a,
        "image2": args.image_b,
    }
    if args.image_c:
        base_body["image3"] = args.image_c

    try:
        data = post_json(url, headers, base_body, args.timeout)
    except urllib.error.HTTPError as first_error:
        if args.no_data_url_fallback:
            raise
        print("direct reference URL failed; retrying with in-memory data URLs", file=sys.stderr)
        retry_body = dict(base_body)
        retry_body["image"] = image_to_data_url(args.image_a)
        retry_body["image2"] = image_to_data_url(args.image_b)
        if args.image_c:
            retry_body["image3"] = image_to_data_url(args.image_c)
        try:
            data = post_json(url, headers, retry_body, args.timeout)
        except urllib.error.HTTPError:
            raise first_error

    image_url = extract_image_url(data)
    if not image_url:
        raise SystemExit("image response did not contain a URL: " + json.dumps(data, ensure_ascii=False)[:1000])
    if image_url.startswith("data:image/"):
        header, encoded = image_url.split(",", 1)
        output = Path(args.out).expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(base64.b64decode(encoded))
    else:
        output = Path(args.out).expanduser().resolve()
        download_url(image_url, output)
    return output


def generate_kolors_text(args) -> Path:
    key = load_key("SILICONFLOW_API_KEY")
    body = {
        "model": args.model or "Kwai-Kolors/Kolors",
        "prompt": args.prompt,
        "image_size": args.size or "1024x1024",
        "batch_size": 1,
    }
    data = post_json(
        "https://api.siliconflow.cn/v1/images/generations",
        {"Authorization": "Bearer " + key, "X-Enable-Watermark": "0"},
        body,
        args.timeout,
    )
    image_url = extract_image_url(data)
    if not image_url:
        raise SystemExit("image response did not contain a URL: " + json.dumps(data, ensure_ascii=False)[:1000])
    output = Path(args.out).expanduser().resolve()
    download_url(image_url, output)
    return output


def generate_generic_json(args) -> Path:
    if not args.endpoint:
        raise SystemExit("--endpoint is required for provider=generic-json")
    if not args.api_key_env:
        raise SystemExit("--api-key-env is required for provider=generic-json")
    key = load_key(args.api_key_env)
    image_a_field = args.image_a_field or "image"
    image_b_field = args.image_b_field or "image2"
    body = {
        args.model_field or "model": args.model,
        args.prompt_field or "prompt": args.prompt,
        image_a_field: args.image_a,
        image_b_field: args.image_b,
    }
    if not args.model:
        body.pop(args.model_field or "model", None)
    if args.image_c:
        body[args.image_c_field or "image3"] = args.image_c
    if args.negative_prompt:
        body[args.negative_prompt_field or "negative_prompt"] = args.negative_prompt
    if args.extra_json:
        try:
            extra = json.loads(args.extra_json)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"invalid --extra-json: {exc}") from exc
        if not isinstance(extra, dict):
            raise SystemExit("--extra-json must be a JSON object")
        body.update(extra)

    headers = {"Authorization": "Bearer " + key}
    if args.auth_header:
        headers = {args.auth_header: args.auth_scheme + " " + key if args.auth_scheme else key}

    try:
        data = post_json(args.endpoint, headers, body, args.timeout)
    except urllib.error.HTTPError as first_error:
        if args.no_data_url_fallback:
            raise
        print("direct reference URL failed; retrying with in-memory data URLs", file=sys.stderr)
        retry_body = dict(body)
        retry_body[image_a_field] = image_to_data_url(args.image_a)
        retry_body[image_b_field] = image_to_data_url(args.image_b)
        if args.image_c:
            retry_body[args.image_c_field or "image3"] = image_to_data_url(args.image_c)
        try:
            data = post_json(args.endpoint, headers, retry_body, args.timeout)
        except urllib.error.HTTPError:
            raise first_error

    image_url = extract_image_url(data)
    if not image_url and args.response_url_path:
        cursor = data
        for part in args.response_url_path.split("."):
            if isinstance(cursor, list):
                cursor = cursor[int(part)]
            else:
                cursor = cursor.get(part)
            if cursor is None:
                break
        if isinstance(cursor, str):
            image_url = cursor
    if not image_url:
        raise SystemExit("image response did not contain a URL: " + json.dumps(data, ensure_ascii=False)[:1000])

    output = Path(args.out).expanduser().resolve()
    if image_url.startswith("data:image/"):
        _, encoded = image_url.split(",", 1)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(base64.b64decode(encoded))
    else:
        download_url(image_url, output)
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description="RefCamera role-separated image generation helper")
    parser.add_argument("--provider", choices=("auto", "siliconflow-qwen-edit", "kolors-text", "generic-json"), default="auto")
    parser.add_argument("--model")
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--image-a", required=True, help="Composition/reference A URL, data URL, or local path")
    parser.add_argument("--image-b", required=True, help="Style/reference B URL, data URL, or local path")
    parser.add_argument("--image-c", help="Optional third reference URL/data URL/path")
    parser.add_argument("--negative-prompt", default="")
    parser.add_argument("--out", required=True)
    parser.add_argument("--size")
    parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--no-data-url-fallback", action="store_true")
    parser.add_argument("--endpoint", help="generic-json endpoint")
    parser.add_argument("--api-key-env", help="generic-json environment variable containing the key")
    parser.add_argument("--auth-header", help="generic-json auth header, default Authorization")
    parser.add_argument("--auth-scheme", default="Bearer", help="generic-json auth scheme; use empty string for raw key")
    parser.add_argument("--model-field", help="generic-json model field, default model")
    parser.add_argument("--prompt-field", help="generic-json prompt field, default prompt")
    parser.add_argument("--image-a-field", help="generic-json A image field, default image")
    parser.add_argument("--image-b-field", help="generic-json B image field, default image2")
    parser.add_argument("--image-c-field", help="generic-json C image field, default image3")
    parser.add_argument("--negative-prompt-field", help="generic-json negative prompt field, default negative_prompt")
    parser.add_argument("--response-url-path", help="dot path to URL if the provider uses a nonstandard response")
    parser.add_argument("--extra-json", help='generic-json JSON object merged into request body, e.g. {"size":"1664x928"}')
    args = parser.parse_args()

    provider = args.provider
    if provider == "auto":
        provider = "siliconflow-qwen-edit"

    if provider == "siliconflow-qwen-edit":
        output = generate_siliconflow_qwen_edit(args)
    elif provider == "kolors-text":
        output = generate_kolors_text(args)
    elif provider == "generic-json":
        output = generate_generic_json(args)
    else:
        raise SystemExit(f"unsupported provider: {provider}")

    print("done:", output)


if __name__ == "__main__":
    main()
