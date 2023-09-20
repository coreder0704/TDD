from __future__ import annotations
from typing import Dict, Tuple
from money import money as mm
from money import expression as me


class Bank:
    def __init__(self) -> None:
        self._rates: Dict[Tuple[str, str], float] = {}


    def reduce(self, source: me.Expression, to: str) -> mm.Money:
        return source.reduce(self, to)


    def add_rate(self, from_cur: str, to_cur: str, rate: int) -> None:
        self._rates[from_cur, to_cur] = rate


    def rate(self, from_cur: str, to_cur: str) -> float:
        if from_cur == to_cur:
            return 1
        return self._rates[from_cur, to_cur]
