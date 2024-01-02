import inflect
import sys

p = inflect.engine()

def main():
    listName = []
    while True:
        try:
            name = input("Name: ").strip().title()
            if name in listName:
                pass
            else:
                listName.append(name)
                pass
        except EOFError:
            mylist = p.join((listName))
            print("\nAdieu, adieu, to", mylist)
            break

main()