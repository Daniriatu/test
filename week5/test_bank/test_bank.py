from bank import value

def test_hello():
    assert value("Hello") == 0


def test_hi():
    assert value("hi") == 20


def test_morning():
    assert value("morning") == 100
