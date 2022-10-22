# pytest
from money import dollar

def  test_multiprication():
    five = dollar.Dollar(5)
    product = five.times(2)
    assert product.amount == 10

    product = five.times(3)
    assert product.amount == 15
