def money(greeting):
    if greeting.startswith("h") == True and "hello" in greeting:
        print("$0")
    elif greeting.startswith("h") == True and "hello" not in greeting:
        print("$20")
    else:
        print("$100")

def main():
    #Interestingly enough, program worked but test didn't return the green smiles if the "Greeting: " bit wasn't included in the input. Huh.
    entry = input("Greeting: ").strip().lower()
    money(entry)

main()