def answer(to):
    if "42" in to or "forty-two" in to or "forty two" in to:
        print("Yes")
    else:
        print("No")

def main():
    wan = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    answer(wan)

main()