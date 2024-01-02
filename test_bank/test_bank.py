from bank import value

def test_bank():
    assert value("hello") == 0
    assert value("heya") == 20
    assert value("greetings") == 100
    assert value("What is up, my dude?") == 100
    assert value("HELLO") == 0
    assert value("HEYA") == 20
    assert value("GREETINGS") == 100

def main():
    test_bank()

if __name__ == "__main__":
    main()