from __future__ import annotations
from money import money as mm
from money import expression as me
from money import sum as ms


class Bank:
    def __init__(self) -> None:
        pass

    def reduce(self, source: me.Expression, to: str) -> mm.Money:
        sum: ms.Sum = source
        amount: int = sum.augend._amount + sum.addend._amount
        return mm.Money(amount, to)
