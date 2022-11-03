from __future__ import annotations

class Dollar:

    def __init__(self, amount: int):
        self.__amount = amount

    def __eq__(self, __o: object) -> bool:
        return self.__dict__ == __o.__dict__ and \
            self.__class__ == __o.__class__

    def times(self, multiplier: int):
        return Dollar(self.__amount * multiplier)

    def equals(self, object: Dollar) -> bool:
        dollar = object
        return self.__amount == dollar.__amount
