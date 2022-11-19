from __future__ import annotations
from money import money

class Franc(money.Money):

    def __init__(self, amount: int) -> None:
        super().__init__(amount)
        self.__currency = "CHF"

    def times(self, multiplier: int) -> money.Money:
        return Franc(self._amount * multiplier)

    def currency(self) -> str:
        return self.__currency
