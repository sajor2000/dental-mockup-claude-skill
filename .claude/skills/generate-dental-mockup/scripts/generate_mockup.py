#!/usr/bin/env python3
"""Generate one patient dental concept image with GPT Image 2."""

import argparse
import base64
import json
import mimetypes
import os
import secrets
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

API_URL = "https://api.openai.com/v1/images/generations"
EDIT_URL = "https://api.openai.com/v1/images/edits"
MODEL = "gpt-image-2"


def decode_image(response: dict) -> bytes:
    try:
        encoded = response["data"][0]["b64_json"]
        return base64.b64decode(encoded, validate=True)
    except (KeyError, IndexError, TypeError, ValueError) as exc:
        raise ValueError("OpenAI response did not contain a valid image") from exc


def self_check() -> None:
    expected = b"\x89PNG\r\n\x1a\n"
    sample = {"data": [{"b64_json": base64.b64encode(expected).decode()}]}
    assert decode_image(sample) == expected
    body, content_type = encode_edit(
        {"model": MODEL, "prompt": "synthetic test"}, "before.png", expected
    )
    assert b"synthetic test" in body and expected in body
    assert content_type.startswith("multipart/form-data; boundary=")
    print("Self-check passed")


def encode_edit(
    fields: dict[str, str], filename: str, image: bytes
) -> tuple[bytes, str]:
    boundary = f"----dental-mockup-{secrets.token_hex(12)}"
    chunks = []
    for name, value in fields.items():
        chunks.append(
            f'--{boundary}\r\nContent-Disposition: form-data; name="{name}"'
            f"\r\n\r\n{value}\r\n".encode()
        )
    content_type = mimetypes.guess_type(filename)[0] or "application/octet-stream"
    chunks.append(
        f'--{boundary}\r\nContent-Disposition: form-data; name="image[]"; '
        f'filename="{Path(filename).name}"\r\nContent-Type: {content_type}'
        f"\r\n\r\n".encode()
        + image
        + b"\r\n"
    )
    chunks.append(f"--{boundary}--\r\n".encode())
    return b"".join(chunks), f"multipart/form-data; boundary={boundary}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prompt")
    parser.add_argument("--input", type=Path, help="Optional patient image to edit")
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--size",
        choices=("auto", "1024x1024", "1536x1024", "1024x1536"),
        default="1024x1024",
    )
    parser.add_argument("--quality", choices=("low", "medium", "high"), default="low")
    parser.add_argument("--self-check", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.self_check:
        self_check()
        return
    if not args.prompt or not args.prompt.strip():
        raise SystemExit("--prompt is required")
    if args.input and (not args.input.is_file() or not os.access(args.input, os.R_OK)):
        raise SystemExit(f"Input image is not readable: {args.input}")
    if args.input and args.input.suffix.lower() not in {
        ".jpg",
        ".jpeg",
        ".png",
        ".webp",
    }:
        raise SystemExit("--input must be a PNG, JPEG, or WebP image")
    if args.input and args.input.stat().st_size > 50 * 1024 * 1024:
        raise SystemExit("--input must be 50 MB or smaller")

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit(
            "OPENAI_API_KEY is not set. Set it in the terminal that launches Claude "
            "Code; do not paste it into chat or save it in the repository."
        )

    output = args.output or Path(
        Path.home(),
        "Data",
        "dental-mockups",
        f"dental-mockup-{datetime.now(timezone.utc):%Y%m%d-%H%M%S}.png",
    )
    if "Dropbox" in output.expanduser().resolve().parts:
        raise SystemExit("Patient images must not be written to Dropbox")
    if output.suffix.lower() != ".png":
        raise SystemExit("--output must end in .png")
    if output.exists():
        raise SystemExit(f"Refusing to overwrite existing file: {output}")

    fields = {
        "model": MODEL,
        "prompt": args.prompt.strip(),
        "size": args.size,
        "quality": args.quality,
    }
    if args.input:
        payload, content_type = encode_edit(
            fields, args.input.name, args.input.read_bytes()
        )
        url = EDIT_URL
    else:
        payload = json.dumps(fields).encode()
        content_type = "application/json"
        url = API_URL
    request = Request(
        url,
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": content_type,
        },
        method="POST",
    )

    try:
        with urlopen(request, timeout=300) as response:
            result = json.load(response)
        image = decode_image(result)
    except HTTPError as exc:
        try:
            message = json.loads(exc.read())["error"]["message"]
        except (json.JSONDecodeError, KeyError, TypeError):
            message = "request failed"
        raise SystemExit(f"OpenAI API error ({exc.code}): {message}") from exc
    except (URLError, TimeoutError) as exc:
        raise SystemExit(
            f"OpenAI API connection failed: {getattr(exc, 'reason', exc)}"
        ) from exc
    except (json.JSONDecodeError, ValueError) as exc:
        raise SystemExit(str(exc)) from exc

    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        with output.open("xb") as file:
            file.write(image)
    except OSError as exc:
        raise SystemExit(f"Could not save image: {exc}") from exc
    print(output.resolve())


if __name__ == "__main__":
    main()
