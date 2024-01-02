import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if twelve := re.search("(1[0-2]|[1-9]):?([0-5][0-9])? (AM|PM) to (1[0-2]|[1-9]):?([0-5][0-9])? (AM|PM)", s):
        hour1 = twelve.group(1)
        hour2 = twelve.group(4)
        hour1 = int(hour1)
        hour2 = int(hour2)
        minute1 = twelve.group(2)
        minute2 = twelve.group(5)
        moment1 = twelve.group(3)
        moment2 = twelve.group(6)
        if hour1 != 12 and hour2 != 12:
            if moment1 == "AM":
                if moment2 == "AM":
                    if minute1:
                        return f"{hour1:02d}:{minute1} to {hour2:02d}:{minute2}"
                    else:
                        return f"{hour1:02d}:00 to {hour2:02d}:00"
                else:
                    hour2 = hour2+12
                    if minute1:
                        return f"{hour1:02d}:{minute1} to {hour2:02d}:{minute2}"
                    else:
                        return f"{hour1:02d}:00 to {hour2:02d}:00"
            else:
                hour1 = hour1+12
                if moment2 == "AM":
                    if minute1:
                        return f"{hour1:02d}:{minute1} to {hour2:02d}:{minute2}"
                    else:
                        return f"{hour1:02d}:00 to {hour2:02d}:00"
                else:
                    hour2 = hour2+12
                    if minute1:
                        return f"{hour1:02d}:{minute1} to {hour2:02d}:{minute2}"
                    else:
                        return f"{hour1:02d}:00 to {hour2:02d}:00"
        else:
            hour1 = 0
            hour2 = 0
            if moment1 == "AM":
                if moment2 == "AM":
                    if minute1:
                        return f"{hour1:02d}:{minute1} to {hour2:02d}:{minute2}"
                    else:
                        return f"{hour1:02d}:00 to {hour2:02d}:00"
                else:
                    hour2 = hour2+12
                    if minute1:
                        return f"{hour1:02d}:{minute1} to {hour2:02d}:{minute2}"
                    else:
                        return f"{hour1:02d}:00 to {hour2:02d}:00"
            else:
                hour1 = hour1+12
                if moment2 == "AM":
                    if minute1:
                        return f"{hour1:02d}:{minute1} to {hour2:02d}:{minute2}"
                    else:
                        return f"{hour1:02d}:00 to {hour2:02d}:00"
                else:
                    hour2 = hour2+12
                    if minute1:
                        return f"{hour1:02d}:{minute1} to {hour2:02d}:{minute2}"
                    else:
                        return f"{hour1:02d}:00 to {hour2:02d}:00"
    else:
        raise ValueError()



if __name__ == "__main__":
    main()
