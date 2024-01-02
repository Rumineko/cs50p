def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    list(s)
    # If length of the list is between 2 and 6
    if len(s) >= 2 and len(s) <= 6:
        # If all entries are alpha-numerical
        if s[0:5].isalnum():
            # If the first two entries are letters
            if s[0:1].isalpha():
                # Restrict range between 3rd entry and the length of the list
                for l in range(2, len(s)):
                    # In case it's a letter:
                    if s[l].isalpha():
                        # Check to make sure we are not on the last item, so we don't get a headache
                        if l < len(s) - 1:
                            # If the item afterwards is a number and not zero
                            if s[l + 1].isdecimal() and s[l + 1] != "0":
                                pass
                            # If the item is a letter
                            elif s[l + 1].isalpha():
                                pass
                            # Oh no, it failed
                            else:
                                return False
                    # (Otherwise) it is not a letter (it's a number, duh)
                    else:
                        # If the number is Zero and the previous entry was a letter
                        if s[l] == "0" and s[l - 1].isalpha():
                            # Omae wa mou shindeiru
                            return False
                        # Once again, just to avoid a headache
                        if l < len(s) - 1:
                            # If it's a bunch more numbers we are fine
                            if s[l + 1].isdecimal():
                                pass
                            # Otherwise into the bin
                            else:
                                return False
                return True
            else:
                return False
        else:
            return False
    else:
        return False


main()
