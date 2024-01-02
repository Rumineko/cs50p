import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search("iframe", s):
         if inp := re.search(r"https?://w?w?w?\.?youtube\.com/embed/([A-Za-z0-9-_]+)", s):
            url = "https://youtu.be/"+ inp.group(1)
            return url


if __name__ == "__main__":
    main()
