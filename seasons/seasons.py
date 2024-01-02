from datetime import date
import re
import inflect
import sys


class Season:
    def __init__(self, year, month, day):
        year = self.year
        month = self.month
        day = self.day

    @classmethod
    def convert(cls, year, month, day):
        year = int(year)
        month = int(month)
        day = int(day)
        p = inflect.engine()
        now = date.today()
        birth = date(year, month, day)
        diff = now - birth
        alive = diff.days*24*60
        return f"{p.number_to_words(int(alive)).capitalize().replace(" and", "")} minutes"


def main():
    if request := re.search("^([0-9][0-9][0-9][0-9])-(1[0-2]|0[1-9])-(3[0-1]|[0-2][0-9])$", input("Date of Birth: ")):
        year = int(request.group(1))
        month = int(request.group(2))
        day = int(request.group(3))
        print(Season.convert(year, month, day))
    else:
        sys.exit("Invalid date")



if __name__ == "__main__":
    main()
