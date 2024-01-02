from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert str(jar.capacity) == "12"
    assert str(jar.size) == "0"


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert str(jar.capacity) == "12"
    jar.deposit(12)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = Jar()
    assert str(jar.capacity) == "12"
    assert str(jar.size) == "0"
    with pytest.raises(ValueError):
        jar.withdraw(1)
