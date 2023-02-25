from __future__ import annotations
from abc import ABCMeta
from money import money as mm


class Expression(metaclass=ABCMeta):
    def reduce(self, to: str) -> mm.Money:
        pass
        # raise NotImprementedError()
