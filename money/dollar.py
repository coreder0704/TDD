from __future__ import annotations
from money import money

class Dollar(money.Money):

    def __init__(self, amount: int, currency: str) -> None:
        super().__init__(amount, currency)

    def times(self, multiplier: int) -> money.Money:
        return Dollar(self._amount * multiplier, self._currency)
