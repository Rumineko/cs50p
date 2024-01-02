from numb3rs import validate

def main():
    test_all

def test_all():
    test_ones
    test_twos
    test_threes

def test_ones():
    assert validate("1.1.1.1") == True
    assert validate("9.9.9.9") == True
    assert validate("0.1.2.3") == True
    assert validate("0.1.2.256") == False

def test_twos():
    assert validate("10.10.10.10") == True
    assert validate("99.99.99.99") == True
    assert validate("0.10.20.30") == True
    assert validate("0.1.2.256") == False

def test_threes():
    assert validate("100.100.100.100") == True
    assert validate("255.255.255.255") == True
    assert validate("0.100.200.255") == True
    assert validate("256.257.258.259") == False

if __name__ == "__main__":
    main()
