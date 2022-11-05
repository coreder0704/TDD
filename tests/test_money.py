# pytest
from money import dollar
from money import franc
from money import money

def  test_multiprication():
    five = money.Money.dollar(5)
    assert five.times(2) == money.Money.dollar(10)
    assert five.times(3) == money.Money.dollar(15)

def test_equality():
    assert money.Money.dollar(5).equals(money.Money.dollar(5))
    assert not money.Money.dollar(5).equals(money.Money.dollar(6))
    assert franc.Franc(5).equals(franc.Franc(5))
    assert not franc.Franc(5).equals(franc.Franc(6))
    assert not franc.Franc(5).equals(money.Money.dollar(5))

def  test_franc_multiprication():
    five = franc.Franc(5)
    assert five.times(2) == franc.Franc(10)
    assert five.times(3) == franc.Franc(15)
