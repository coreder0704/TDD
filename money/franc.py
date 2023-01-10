from __future__ import annotations
from money import money as mm


class Franc(mm.Money):

    def __init__(self, amount: int, currency: str) -> None:
        super().__init__(amount, currency)
