from __future__ import annotations

class Dollar:

    def __init__(self, amount: int):
        self._amount = amount

    def __eq__(self, other: Dollar) -> bool:
        return self.__dict__ == other.__dict__ and \
            self.__class__ == other.__class__

    def times(self, multiplier: int) -> Dollar:
        return Dollar(self._amount * multiplier)

    def equals(self, other: Dollar) -> bool:
        return self._amount == other._amount
