import sys
from PIL import Image
from PIL import ImageOps

def main():
    sys_check()
    using_image()



def using_image():
    try:
        imageFile = Image.open(sys.argv[1])

    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    muppet = ImageOps.fit(imageFile, size)
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2])


def sys_check():
    file1 = sys.argv[1].split(".")
    file2 = sys.argv[2].split(".")

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid output")

    if not sys.argv[2].lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid output")

    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
