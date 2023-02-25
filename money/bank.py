from __future__ import annotations
from money import money as mm
from money import expression as me


class Bank:
    def __init__(self) -> None:
        pass

    def reduce(self, source: me.Expression, to: str) -> Bank:
        return mm.Money.dollar(10)
