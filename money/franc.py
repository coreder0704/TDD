from __future__ import annotations

class Franc():

    def __init__(self, amount: int):
        self._amount = amount

    def __eq__(self, other: Franc) -> bool:
        return self.__dict__ == other.__dict__ and \
            self.__class__ == other.__class__

    def times(self, multiplier: int) -> Franc:
        return Franc(self._amount * multiplier)

    def equals(self, other: Franc) -> bool:
        return self._amount == other._amount
