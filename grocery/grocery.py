def main():
    # Create an empty dictionary, which will be our shopping list
    list = {

    }
    # Create a loop until we break out of it with CTRL+D
    while True:
        try:
            # Request item from user
            item = input("").strip().upper()
            # Check if it's in our list, if it is then +1
            if item in list:
                list[item] += 1
            # If not then it's fine, we create an entry and make it equal to 1
            elif item not in list:
                list[item] = 1
        # If we end the program with CTRL+D
        except EOFError:
            # First we sort the list, alphabetically
            sorted_list = dict(sorted(list.items()))
            # And then we use a for loop to print every item, with its quantity first
            for i in sorted_list:
                print(f"{sorted_list[i]} {i}")
            # And we break the loop, so program ends.
            break

main()