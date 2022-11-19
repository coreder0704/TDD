from __future__ import annotations
from money import money

class Franc(money.Money):

    def times(self, multiplier: int) -> money.Money:
        return Franc(self._amount * multiplier)

    def currency(self) -> str:
        return "CHF"
