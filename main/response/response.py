import sys
import validators


def main():
    validate(input("What's your email address? "))


def validate(s):
    if validators.email(s) == True:
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
