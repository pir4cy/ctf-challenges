#!/usr/bin/env python3

import argparse
import random
import shutil
import subprocess
import sys
from pathlib import Path

DESCRIPTIONS = [
    "A quiet afternoon in the city",
    "Remembering this little moment",
    "A walk through the old streets",
    "Taken during the weekend trip",
    "One of my favourite places",
    "A beautiful day to be outside",
    "Nothing special, just a photograph",
    "Exploring somewhere new",
    "A quick stop along the way",
    "Captured on the way home",
    "Another memory worth keeping",
    "The view from that afternoon",
    "A small detail I almost missed",
    "An unexpected little adventure",
    "Just another day out",
    "A place I would visit again",
    "The light was perfect that day",
    "A moment from the journey",
    "Found this spot by accident",
    "One last picture before leaving",
]


def main():
    parser = argparse.ArgumentParser(
        description="Prepare the Camera Lost & Found CTF challenge."
    )
    parser.add_argument("input_dir", help="Directory containing source images")
    parser.add_argument("output_dir", help="Directory for challenge images")
    parser.add_argument(
        "--flag-url",
        default="https://example.com/flag.txt",
        help="URL to embed in EXIF metadata (flag is fetched from this link)",
    )
    args = parser.parse_args()

    source = Path(args.input_dir).resolve()
    output = Path(args.output_dir).resolve()

    if not source.is_dir():
        sys.exit(f"[!] Input directory does not exist: {source}")

    if source == output or source in output.parents:
        sys.exit("[!] Output must not be the input directory or a subdirectory of it.")

    if not shutil.which("exiftool"):
        sys.exit("[!] ExifTool not found. Install it with: sudo apt install libimage-exiftool-perl")

    extensions = {".jpg", ".jpeg"}
    images = sorted(
        p for p in source.iterdir()
        if p.is_file() and p.suffix.lower() in extensions
    )

    if not images:
        sys.exit("[!] No JPEG images found in the input directory.")

    if not args.flag_url.strip():
        sys.exit("[!] Flag URL cannot be empty.")

    output.mkdir(parents=True, exist_ok=True)

    # Choose exactly one image to contain the flag.
    flag_image = random.SystemRandom().choice(images)

    print(f"[*] Found {len(images)} JPEG images.")
    print(f"[*] Preparing challenge in: {output}")

    try:
        for image in images:
            destination = output / image.name
            shutil.copy2(image, destination)

            if image == flag_image:
                description = args.flag_url
            else:
                description = random.choice(DESCRIPTIONS)

            subprocess.run(
                [
                    "exiftool",
                    "-overwrite_original",
                    f"-ImageDescription={description}",
                    str(destination),
                ],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
                text=True,
            )

            print(f"[+] Processed: {image.name}")

    except (subprocess.CalledProcessError, OSError) as error:
        sys.exit(f"[!] Failed to process images: {error}")

    # Verify the flag URL is actually present in the selected image.
    result = subprocess.run(
        ["exiftool", "-s3", "-ImageDescription", str(output / flag_image.name)],
        capture_output=True,
        text=True,
        check=True,
    )

    if result.stdout.strip() != args.flag_url:
        sys.exit("[!] Verification failed: flag URL metadata does not match.")

    print("\n[+] Challenge prepared successfully!")
    print(f"[+] Total images: {len(images)}")
    print(f"[+] Flag image (keep this private): {flag_image.name}")
    print(f"[+] Flag URL: {args.flag_url}")


if __name__ == "__main__":
    main()
