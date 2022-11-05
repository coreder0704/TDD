# pytest
from money import money

def  test_multiprication():
    five = money.Money.dollar(5)
    assert five.times(2) == money.Money.dollar(10)
    assert five.times(3) == money.Money.dollar(15)

def test_equality():
    assert money.Money.dollar(5).equals(money.Money.dollar(5))
    assert not money.Money.dollar(5).equals(money.Money.dollar(6))

    assert money.Money.franc(5).equals(money.Money.franc(5))
    assert not money.Money.franc(5).equals(money.Money.franc(6))

    assert not money.Money.franc(5).equals(money.Money.dollar(5))

def  test_franc_multiprication():
    five = money.Money.franc(5)
    assert five.times(2) == money.Money.franc(10)
    assert five.times(3) == money.Money.franc(15)
