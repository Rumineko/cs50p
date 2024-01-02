import sys
from tabulate import tabulate
import csv

def main():
    pizza = []
    while True:
        try:
            if len(sys.argv) < 2:
                sys.exit("Too few command-line arguments")
            elif len(sys.argv) > 2:
                sys.exit("Too many command-line arguments")
            else:
                path = sys.argv[1]
                if path.endswith(".csv"):
                    with open(f"{path}", "r") as file:
                        lines = csv.reader(file)
                        for line in lines:
                            pizza.append(line)
                        headers = pizza[0]
                        del pizza[0]
                        print(tabulate(pizza, headers, tablefmt="grid"))
                        break
                else:
                    sys.exit("Not a CSV file")
        except FileNotFoundError:
            sys.exit("File does not exist")


if __name__ == "__main__":
    main()