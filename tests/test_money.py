# pytest
from money import dollar

def  test_multiprication():
    five = dollar.Dollar(5)
    product = five.times(2)
    assert product == dollar.Dollar(10)

    product = five.times(3)
    assert product.amount == 15

def test_equality():
    assert dollar.Dollar(5).equals(dollar.Dollar(5))
    assert not dollar.Dollar(5).equals(dollar.Dollar(6))
