import os, sys

from pathlib import Path
from PIL import Image


def convert_to_webp(source):
    """Convert image to WebP.

    Args:
        source (pathlib.Path): Path to source image

    Returns:
        pathlib.Path: path to new image
    """
    destination = source.with_suffix(".webp")

    image = Image.open(source)  # Open image
    image.save(destination, format="webp")  # Convert image to webp

    return destination


if __name__ == "__main__":

    img_types = ("png", "jpg", "jpeg")

    if len(sys.argv) == 3 and sys.argv[1] == "--path" and os.path.isdir(sys.argv[2]):

        for type in img_types:

            paths = Path(sys.argv[2]).glob("**/*.%s" % type)

            for path in paths:
                print(path)
                webp_path = convert_to_webp(path)
                print(webp_path)

    else:

        print("Usage: python3 webp.py --path [PATH TO CONVERT IMAGES TO WEBP]")
