def main():
    query = input("Fraction: ").strip()
    percent = convert(query)
    print(gauge(percent))

def convert(fraction):
    x, y = fraction.strip().split("/")
    x = int(x)
    y = int(y)
    percent = round((x / y) * 100)
    return percent

def gauge(percentage):
    Z = int(percentage)
    if Z <= 1:
        return("E")
    # Otherwise if it's more or equal to 99 it will be full
    elif Z >= 99:
        return("F")
    # OTHERWISE it will just print the percentage with a %
    else:
        return(f"{Z}%")


if __name__ == "__main__":
    main()