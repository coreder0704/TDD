from __future__ import annotations
from money import money

class Franc(money.Money):

    def __init__(self, amount: int, currency: str) -> None:
        super().__init__(amount, currency)
