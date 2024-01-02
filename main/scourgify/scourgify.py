import sys
import csv

def main():
    names = []
    while True:
        try:
            if len(sys.argv) < 2:
                sys.exit("Too few command-line arguments")
            elif len(sys.argv) > 3:
                sys.exit("Too many command-line arguments")
            else:
                path1 = sys.argv[1]
                path2 = sys.argv[2]
                if path1.endswith(".csv") and path2.endswith("csv"):
                    with open(f"{path1}", "r") as file1:
                        lines = csv.DictReader(file1)
                        for line in lines:
                            last, first = line["name"].split(",")
                            first = first.replace(" ", "")
                            house = line["house"]
                            names.append({'first': first, 'last' : last, 'house': house})
                        with open(f"{path2}", "w") as file2:
                            fieldnames = ["first", "last" , "house"]
                            writer = csv.DictWriter(file2, fieldnames=fieldnames)
                            writer.writeheader()
                            for name in names:
                                writer.writerow(name)
                            break
                else:
                    sys.exit(f"Could not read {sys.argv[1]}")
        except FileNotFoundError:
            sys.exit("File does not exist")

if __name__ == "__main__":
    main()