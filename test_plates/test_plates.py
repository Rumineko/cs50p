from plates import is_valid

def main():
    test_plates()

# HA, this is actually incredibly useful. Turns out there was a bug in my initial code of plates.py in line 16, which I only
# found because of debugging and testing like this. This has been very enlightening, thank you CS50
def test_plates():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("LOVEME") == True
    assert is_valid("AB1234") == True
    assert is_valid("AB0123") == False
    assert is_valid("A01234") == False
    assert is_valid("012345") == False
    assert is_valid("A") == False
    assert is_valid("1A") == False
    assert is_valid("AA") == True
    assert is_valid("11") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("AB12345") == False
    assert is_valid("AB!234") == False
    assert is_valid("AB1C2D") == False
    assert is_valid("!12345") == False


if __name__ == "__main__":
    main()