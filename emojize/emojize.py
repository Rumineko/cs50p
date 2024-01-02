import emoji

def main():
    emo = input("Input: ").strip()
    print(emoji.emojize(emo, language='alias'))

main()