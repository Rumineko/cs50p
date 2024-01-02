from seasons import Season

def main():
    test_season

def test_season():
    assert Season.convert("1998", "09", "30") == "Thirteen million, two hundred thirty-six thousand, four hundred eighty minutes"
    assert Season.convert("1998", "10", "09") == "Thirteen million, two hundred twenty-three thousand, five hundred twenty minutes"

if __name__ == "__main__":
    main()
