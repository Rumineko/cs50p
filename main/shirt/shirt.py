import sys
from PIL import Image, ImageOps
import os

def main():
    while True:
        try:
            if len(sys.argv) < 3:
                sys.exit("Too few command-line arguments")
            elif len(sys.argv) > 3:
                sys.exit("Too many command-line arguments")
            else:
                name1, ext1 = os.path.splitext(f"{sys.argv[1]}")
                name2, ext2 = os.path.splitext(f"{sys.argv[2]}")
                ext1 = ext1.lower()
                ext2 = ext2.lower()
                if ext1 == "":
                    sys.exit("Invalid input")
                elif ext2 == "":
                    sys.exit("Invalid output")
                elif ext1 != ext2:
                    sys.exit("Input and output have different extensions")
                else:
                    shirt = Image.open("shirt.png")
                    size = shirt.size
                    subject = Image.open(f"{sys.argv[1]}")
                    subject = ImageOps.fit(subject, size)
                    subject.paste(shirt, (0,0), mask=shirt)
                    subject.save(sys.argv[2])
                    break
        except FileNotFoundError:
            sys.exit("Input does not exist")


if __name__ == "__main__":
    main()