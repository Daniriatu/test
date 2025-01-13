from jar import Jar
import pytest


def test_init():
    jar_one = Jar()
    assert jar_one.capacity == 12
    assert jar_one.size == 0
    
    jar_two = Jar(4)
    assert jar_two.capacity == 4
    assert jar_two.size == 0

    with pytest.raises(ValueError):
        jar_three = Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(3)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    
    with pytest.raises(ValueError):
        jar.deposit(10)


def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(3)
    assert str(jar) == ""
    
    with pytest.raises(ValueError):
        jar.withdraw(1)