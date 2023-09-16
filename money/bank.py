from __future__ import annotations
from money import money as mm
from money import expression as me
from money import sum as ms


class Bank:
    def __init__(self) -> None:
        pass


    def reduce(self, source: me.Expression, to: str) -> mm.Money:
        return source.reduce(to)


    def add_rate(self, from_cur: str, to_cur: str, rate: int) -> None:
        pass
