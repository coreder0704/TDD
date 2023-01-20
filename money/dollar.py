from __future__ import annotations
from money import money as mm

class Dollar(mm.Money):

    def __init__(self, amount: int, currency: str) -> None:
        super().__init__(amount, currency)
