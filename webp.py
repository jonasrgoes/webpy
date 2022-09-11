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
    destination = "%s.%s" % (source, "webp")

    image = Image.open(source)  # Open image
    image.save(destination, format="webp")  # Convert image to webp

    return destination


def convert_images(dir: str, overwrite: bool = False):

    img_types = ("png", "jpg", "jpeg")

    for type in img_types:

        paths = Path(dir).glob("**/*.%s" % type)

        with open("log.txt", "a+") as file_object:

            for path in paths:

                if overwrite == False and os.path.isfile("%s.%s" % (path, "webp")):
                    # print("Image already converted: %s" % path)
                    continue

                try:
                    webp_path = convert_to_webp(path)
                    file_object.write(webp_path + "\n")
                    print("Converted: %s" % webp_path)
                except Exception as e:
                    print("Unable to convert %s to webp: %s" % (path, e))


if __name__ == "__main__":

    img_types = ("png", "jpg", "jpeg")

    if len(sys.argv) == 3 and sys.argv[1] == "--path" and os.path.isdir(sys.argv[2]):

        convert_images(dir=sys.argv[2])

    elif (
        len(sys.argv) == 4
        and sys.argv[1] == "--path"
        and os.path.isdir(sys.argv[2])
        and sys.argv[3] == "--overwrite"
    ):

        convert_images(dir=sys.argv[2], overwrite=True)

    else:

        print("Usage: python3 webp.py --path [PATH TO CONVERT IMAGES TO WEBP]")
        print(
            "Usage: python3 webp.py --path [PATH TO CONVERT IMAGES TO WEBP] --overwrite"
        )
