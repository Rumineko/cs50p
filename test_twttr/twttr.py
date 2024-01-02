# Our main will create a str and run it through a function we will create, called twttr
def main():
    npt = input("Input: ").strip()
    print(shorten(npt))

# Here's our twttr. It will take the string, make a list with it, and run it through some filters
def shorten(word):
    list(word)
    # Don't forget to yeet a string in there
    yeet = ""
    for t in word:
        # Lowercase just in case someone forgets to turn off their CAPS LOCK
        if t.lower() == "a" or t.lower() == "e" or t.lower() == "i" or t.lower() == "o" or t.lower() == "u":
            continue
        # You're welcome to the club as long as you're not a vowel
        else:
            yeet += t
    # Perfection.
    return yeet

if __name__ == "__main__":
    main()