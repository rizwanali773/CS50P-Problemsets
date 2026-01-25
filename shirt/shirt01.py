import sys

from PIL import Image
from PIL import ImageOps

file1 = sys.argv[1].split(".")
file2 = sys.argv[2].split(".")

if file1[1].lower() != file2[1].lower():
        print("Input and output have different extensions")
        sys.exit(1)


if len(sys.argv) < 3:
    print("Too few cpmmand-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many many command-line arguments")
    sys.exit(1)
elif not((sys.argv[1].lower().endswith(".jpeg") and sys.argv[2].lower().endswith(".jpeg")) or (sys.argv[1].lower().endswith(".jpg") and sys.argv[2].lower().endswith(".jpg")) or (sys.argv[1].lower().endswith(".png") and sys.argv[2].lower().endswith(".png"))):
    print("Input and output have different extensions")
    sys.exit(1)
else:
    try:
        first_image = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        size = shirt.size
        muppet = Image.copy(first_image)
        image = ImageOps.fit(muppet, size)
        image = image.past(shirt, shirt)
        image.save(sys.argv[2])
    except FileNotFoundError:
        print("Input does not exist")
        sys.exit(1)

