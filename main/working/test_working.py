from working import convert
import pytest

def main():
    test_all

def test_all():
    test_twelves
    test_mixes
    test_ams
    test_pms
    test_others

def test_twelves():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("12:30 AM to 12:30 PM") == "00:30 to 12:30"
    assert convert("12:30 PM to 12:30 AM") == "12:30 to 00:30"


def test_mixes():
    assert convert("10 AM to 10 PM") == "10:00 to 22:00"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"
    assert convert("9:30 PM to 5:30 AM") == "21:30 to 05:30"

def test_ams():
    assert convert("1 AM to 10 AM") == "01:00 to 10:00"
    assert convert("10:30 AM to 1:30 AM") == "10:30 to 01:30"

def test_pms():
    assert convert("1 PM to 10 PM") == "13:00 to 22:00"
    assert convert("10:30 PM to 1:30 PM") == "22:30 to 13:30"

def test_others():
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")

if __name__ == "__main__":
    main()
