from __future__ import annotations
from money import money

class Franc(money.Money):

    def times(self, multiplier: int) -> Franc:
        return Franc(self._amount * multiplier)
