from __future__ import annotations
from money import money

class Dollar(money.Money):

    def times(self, multiplier: int) -> Dollar:
        return Dollar(self._amount * multiplier)
