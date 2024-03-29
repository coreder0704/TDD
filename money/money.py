from __future__ import annotations
from typing import Any
from money import expression as me
from money import sum as ms
from money import bank as mb

class Money(me.Expression):

    def __init__(self, amount: float, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def __eq__(self, other: Any) -> bool:
        return self.__dict__ == other.__dict__ and \
            self.__class__ == other.__class__

    def equals(self, other: Money) -> bool:
        return self._amount == other._amount and \
            self._currency == other._currency

    def __str__(self) -> str:
        return f"{self._amount} {self._currency}"

    __repr__ = __str__

    def times(self, multiplier: int) -> me.Expression:
        return Money(self._amount * multiplier, self._currency)

    def currency(self) -> str:
        return self._currency


    def plus(self, addend: me.Expression) -> me.Expression:
        return ms.Sum(self, addend)


    def reduce(self, bank: mb.Bank, to: str) -> Money:
        rate: float = bank.rate(self._currency, to)
        return Money(self._amount / rate, to)


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
