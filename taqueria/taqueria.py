def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    tab = 0.00
    while True:
        try:
            item = input("Item: ").strip().title()
            if item in menu:
                cost = menu.get(f"{item}")
                if cost is not None:
                    cost = float(cost)
                    tab = tab + cost
                    print(f"Total: ${tab:.2f}")
                else:
                    pass
            else:
                pass
        except EOFError:
            break

main()