# pytest
from TDD.money import dollar

def  test_multiprication():
    five = dollar.Dollar(5)
    five.times(2)
    assert five.amount == 10
