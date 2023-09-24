# pytest
from money import money as mm
from money import bank as mb
from money import expression as me
from money import sum as ms


def test_multiprication():
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


def test_addition():
    five: mm.Money = mm.Money.dollar(5)
    sum: me.Expression = five.plus(mm.Money.dollar(5))
    bank: mb.Bank = mb.Bank()
    reduced: mm.Money = bank.reduce(sum, "USD")
    assert reduced == mm.Money.dollar(10)


def test_plus_returns_sum():
    five: mm.Money = mm.Money.dollar(5)
    result: me.Expression = five.plus(five)
    sum: ms.Sum = result
    assert five == sum.augend
    assert five == sum.addend


def test_reduce_sum():
    sum: ms.Sum = ms.Sum(mm.Money.dollar(3), mm.Money.dollar(4))
    bank: mb.Bank = mb.Bank()
    result: mm.Money = bank.reduce(sum, "USD")
    assert result == mm.Money.dollar(7)


def test_reduce_money():
    bank: mb.Bank = mb.Bank()
    result: mm.Money = bank.reduce(mm.Money.dollar(1), "USD")
    assert result == mm.Money.dollar(1)


def test_reduce_money_different_currency():
    bank: mb.Bank = mb.Bank()
    bank.add_rate("CHF", "USD", 2)
    result: mm.Money = bank.reduce(mm.Money.franc(2), "USD")
    assert result == mm.Money.dollar(1)


# for learning
def test_array_equals():
    assert ["abc"] == ["abc"]


# for learning
def test_two_keys_to_dictionary():
    rates = {}
    from_cur = "CHF"
    to_cur = "USD"
    rates[from_cur, to_cur] = 2
    assert rates["CHF", "USD"] == 2


def test_identify_rate():
    assert mb.Bank().rate("USD", "USD") == 1


def test_mixed_addition():
    five_bucks: me.Expression = mm.Money.dollar(5)
    ten_francs: me.Expression = mm.Money.franc(10)
    bank: mb.Bank = mb.Bank()
    bank.add_rate("CHF", "USD", 2)
    result: mm.Money = bank.reduce(five_bucks.plus(ten_francs), "USD")
    assert result == mm.Money.dollar(10)


def test_sum_plus_money():
    five_bucks: me.Expression = mm.Money.dollar(5)
    ten_francs: me.Expression = mm.Money.franc(10)
    bank: mb.Bank = mb.Bank()
    bank.add_rate("CHF", "USD", 2)
    sum1: me.Expression = ms.Sum(five_bucks, ten_francs).plus(five_bucks)
    result1: mm.Money = bank.reduce(sum1, "USD")
    assert result1 == mm.Money.dollar(15)
    sum2: me.Expression = ms.Sum(five_bucks, ten_francs).plus(ten_francs)
    result2: mm.Money = bank.reduce(sum2, "USD")
    assert result2 == mm.Money.dollar(15)


def test_sum_times():
    five_bucks: me.Expression = mm.Money.dollar(5)
    ten_francs: me.Expression = mm.Money.franc(10)
    bank: mb.Bank = mb.Bank()
    bank.add_rate("CHF", "USD", 2)
    sum1: me.Expression = ms.Sum(five_bucks, ten_francs).times(2)
    result1: mm.Money = bank.reduce(sum1, "USD")
    assert result1 == mm.Money.dollar(20)


def test_plus_same_currency_return_money():
    sum: me.Expression = mm.Money.dollar(5).plus(mm.Money.dollar(5))
    assert isinstance(sum, mm.Money)
