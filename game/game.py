from random import randint
import sys

def main():
    while True:
        try:
            level = int(input("Level: ").strip())
            number = randint(1, level)
            break
        except ValueError:
            pass
    while True:
        try:
            guess = int(input("Guess: ").strip())
            if guess > number:
                print("Too large!")
            elif guess < number:
                print ("Too small!")
            else:
                sys.exit("Just right!")
        except ValueError:
            pass

main()