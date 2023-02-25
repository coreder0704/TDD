from __future__ import annotations
from money import expression as me
from money import sum as ms

class Money(me.Expression):

    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def __eq__(self, other: Money) -> bool:
        return self.__dict__ == other.__dict__ and \
            self.__class__ == other.__class__

    def equals(self, other: Money) -> bool:
        return self._amount == other._amount and \
            self._currency == other._currency

    def __str__(self) -> str:
        return f"{self._amount} {self._currency}"

    __repr__ = __str__

    def times(self, multiplier: int) -> Money:
        return Money(self._amount * multiplier, self._currency)

    def currency(self) -> str:
        return self._currency


    def plus(self, addend: Money) -> me.Expression:
        return ms.Sum(self, addend)


    def reduce(self, to: str) -> Money:
        return self


    @staticmethod
    def dollar(amount: int) -> Money:
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int) -> Money:
        return Money(amount, "CHF")

if __name__ == "__main__":
    # test __str__()
    money = Money.dollar(1)
    print(money)
    print(money.times(2) == Money.dollar(2))

    money2 = Money.franc(1)
    print(money2)
    print(money2.times(2) == Money.franc(2))
