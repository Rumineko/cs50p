def convert(to):
    to = to.replace(":)", "🙂").replace(":(", "🙁")
    return to

def main():
    quote = input()
    print(convert(quote))

main()