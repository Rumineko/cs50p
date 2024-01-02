import sys

def main():
    number = 0
    while True:
        try:
            if len(sys.argv) < 2:
                sys.exit("Too few command-line arguments")
            elif len(sys.argv) > 2:
                sys.exit("Too many command-line arguments")
            else:
                path = sys.argv[1]
                if path.endswith(".py"):
                    with open(f"{path}", "r") as file:
                        lines = file.readlines()

                    for line in lines:
                        line = line.strip()
                        if line != "" and line.startswith("#") == False:
                            number += 1
                    print(number)
                    break
                else:
                    sys.exit("Not a Python file")
        except FileNotFoundError:
            sys.exit("File does not exist")



if __name__ == "__main__":
    main()