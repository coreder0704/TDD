from __future__ import annotations
from money import money as mm
from money import expression as me
from money import bank as mb


class Sum(me.Expression):
    def __init__(self, augend: mm.Money, addend:mm.Money) -> None:
        self.augend:mm.Money = augend
        self.addend:mm.Money = addend


    def reduce(self, bank: mb.Bank, to: str) -> mm.Money:
        amount: float = self.augend.reduce(bank, to)._amount \
              + self.addend.reduce(bank, to)._amount
        return mm.Money(amount, to)
