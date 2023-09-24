from __future__ import annotations
from abc import ABCMeta
from money import money as mm
from money import bank as mb


class Expression(metaclass=ABCMeta):
    def plus(self, addend: Expression) -> Expression:
        pass


    def times(self, multiplier: int) -> Expression:
        pass


    def reduce(self, bank: mb.Bank, to: str) -> mm.Money:
        pass
        # raise NotImprementedError()
