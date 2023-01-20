# pytest
from money import money as mm

def  test_multiprication():
    five = mm.Money.dollar(5)
    assert five.times(2).equals(mm.Money.dollar(10))
    assert five.times(3).equals(mm.Money.dollar(15))


def test_equality():
    assert mm.Money.dollar(5).equals(mm.Money.dollar(5))
    assert not mm.Money.dollar(5).equals(mm.Money.dollar(6))
    assert not mm.Money.franc(5).equals(mm.Money.dollar(5))


def test_currency():
    assert "USD" == mm.Money.dollar(1).currency()
    assert "CHF" == mm.Money.franc(1).currency()
