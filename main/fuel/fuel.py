def main():
    # We call the get_percent function we create
    percentage = get_percent()
    # If it is less to or equal than 1 it will be Empty
    if percentage <= 1:
        print("E")
    # Otherwise if it's more or equal to 99 it will be full
    elif percentage >= 99:
        print("F")
    # OTHERWISE it will just print the percentage with a %
    else:
        print(f"{percentage}%")

def get_percent():
    while True:
        try:
            # We split the input into two strings, x and y
            x, y = input("Fraction: ").strip().split("/")
            # Ensure we turn x and y into integers so that we can divide them
            x = int(x)
            y = int(y)
            # Divide them and make them a percentage
            percent = (x / y) * 100
            # Round our float and turn it into an integer
            percent = round(percent)
            # In case we get a value over 100%, it will reprompt, otherwise return value and break out of loop
            if percent <= 100:
                return percent
            else:
                pass
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()