from __future__ import annotations
from money import money as mm
from money import expression as me


class Sum(me.Expression):
    def __init__(self, augend: mm.Money, addend:mm.Money) -> None:
        self.augend:mm.Money = augend
        self.addend:mm.Money = addend
