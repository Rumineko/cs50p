from fuel import convert
from fuel import gauge
import pytest

def main():
    test_convert()
    test_gauge()
    test_errors()

def test_errors():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("x/y")

def test_convert():
    assert convert("1/4") == 25
    assert convert("1/3") == 33
    assert convert("2/4") == 50
    assert convert("2/3") == 67
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert convert("1/100") == 1
    assert convert("0/1") == 0
    assert convert("99/100") == 99

def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"


if __name__ == "__main__":
    main()