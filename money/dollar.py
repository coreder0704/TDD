from __future__ import annotations
from money import money

class Dollar(money.Money):

    def __init__(self, amount: int) -> None:
        super().__init__(amount)
        self._currency = "USD"

    def times(self, multiplier: int) -> money.Money:
        return Dollar(self._amount * multiplier)
