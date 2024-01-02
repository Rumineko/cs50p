def main():
    # We request our fruit from the user
    fruit = input("Fruit: ").strip().lower()

    # Here is our Nutrition dictionary
    nutrition = {
        "apple" : "130",
        "avocado" : "50",
        "banana" : "110",
        "cantaloupe" : "50",
        "grapefruit" : "60",
        "grapes" : "90",
        "honeydew" : "50",
        "kiwifruit" : "90",
        "lemon" : "15",
        "lime" : "20",
        "nectarine" : "60",
        "orange" : "80",
        "peach" : "60",
        "pear" : "100",
        "pineapple" : "50",
        "plums" : "70",
        "strawberries" : "50",
        "sweet cherries" : "100",
        "tangerine" : "50",
        "watermelon" : "80",
    }

    # We replace the str with its correspondent dictionary entry
    fruit = nutrition.get(f"{fruit}")

    # And then we need to ensure that the Fruit exists. If there is no entry for it, it won't output anything
    if fruit == None:
        print("")
    else:
        print(f"Calories: {fruit}")

main()