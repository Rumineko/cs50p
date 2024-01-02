def main():
    #Interestingly enough, program worked but test didn't return the green smiles if the "Greeting: " bit wasn't included in the input. Huh.
    entry = input("Greeting: ").strip().lower()
    print(f"${value(entry)}")

def value(greeting):
    if greeting.startswith("h") == True and "hello" in greeting:
        return 0
    elif greeting.startswith("h") == True and "hello" not in greeting:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()