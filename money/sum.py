from __future__ import annotations
from money import money as mm
from money import expression as me
from money import bank as mb


class Sum(me.Expression):
    def __init__(self, augend: me.Expression, addend:me.Expression) -> None:
        self.augend:me.Expression = augend
        self.addend:me.Expression = addend


    def plus(self, addend: me.Expression) -> me.Expression:
        pass


    def reduce(self, bank: mb.Bank, to: str) -> mm.Money:
        amount: float = self.augend.reduce(bank, to)._amount \
              + self.addend.reduce(bank, to)._amount
        return mm.Money(amount, to)
