import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()
randFont = random.choice(fonts)

def main():
    if len(sys.argv) == 1:
        figlet.setFont(font=randFont)
        print(figlet.renderText(input("Input: ").strip()))
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "-font":
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(input("Input: ").strip()))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

main()