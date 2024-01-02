import random

def main():
    correct = 0
    problems = 0
    mistakes = 0
    diff = get_level()
    a = generate_integer(diff)
    b = generate_integer(diff)
    c = a + b
    while problems < 10:
        try:
            if mistakes == 3:
                problems += 1
                mistakes = 0
                print(f"{a} + {b} = {c}")
                a = generate_integer(diff)
                b = generate_integer(diff)
                c = a + b
            else:
                pass
            guess = input(f"{a} + {b} = ")
            if guess.isalpha():
                print("EEE")
                mistakes += 1
            else:
                pass
            numguess = int(guess)
            if numguess == c:
                correct += 1
                problems += 1
                mistakes = 0
                a = generate_integer(diff)
                b = generate_integer(diff)
                c = a + b
            else:
                print("EEE")
                mistakes += 1
        except ValueError:
            pass
    if problems == 10:
        print(f"Score: {correct}")


def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
            if level == 1:
                return 9
            elif level == 2:
                return 99
            elif level == 3:
                return 999
            else:
                pass
        except ValueError:
            pass


def generate_integer(level):
    if level == 9:
        return random.randint(0, level)
    elif level == 99:
        return random.randint(10, level)
    elif level == 999:
        return random.randint(100, level)


if __name__ == "__main__":
    main()