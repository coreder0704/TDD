# pytest
from money import dollar
from money import franc

def  test_multiprication():
    five = dollar.Dollar(5)
    assert five.times(2) == dollar.Dollar(10)
    assert five.times(3) == dollar.Dollar(15)

def test_equality():
    assert dollar.Dollar(5).equals(dollar.Dollar(5))
    assert not dollar.Dollar(5).equals(dollar.Dollar(6))

def  test_franc_multiprication():
    five = franc.Franc(5)
    assert five.times(2) == franc.Franc(10)
    assert five.times(3) == franc.Franc(15)
