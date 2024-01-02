def main():
    time = input("What time is it? ").strip()
    food = convert(time)
    if food >= 7 and food <= 8:
        print("breakfast time")
    elif food >= 12 and food <= 13:
        print("lunch time")
    elif food >= 18 and food <= 19:
        print("dinner time")
    else:
        print()


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes) / 60
    oclock = float(hours + minutes)
    return oclock


if __name__ == "__main__":
    main()