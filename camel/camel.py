# Start by definining main
def main():
    # Create str camel, takes user input and strips whitespace
    camel = input("camelCase: ").strip()
    # We then create a str snake, which will take a future function snakecase to convert our input, camel, into snake_case
    snake = snakecase(camel)
    # Print snake
    print("snake_case: " + snake)

# Now we move on to making snakecase
def snakecase(query):
    # We first convert our input into a list, separating every letter into a different item in the list
    list(query)
    # Create an empty string where we will convert our input into snakecase
    scase = ""
    # Using our list with a for function
    for l in query:
        # If the item it's currently looking at is uppercase
        if l.isupper():
            # It then instead first adds an underscore_ and then the letter but in lowercase
            scase += "_" + l.lower()
        # Otherwise
        else:
            # Same old, same old
            scase += l
    # And return our string once fully converted
    return scase

main()