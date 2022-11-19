from __future__ import annotations

class Money:

    def __init__(self, amount: int):
        self._amount = amount

    def __eq__(self, other: Money) -> bool:
        return self.__dict__ == other.__dict__ and \
            self.__class__ == other.__class__

    def equals(self, other: Money) -> bool:
        return self._amount == other._amount and \
            self.__class__ == other.__class__

    def currency() -> str:
        pass

    @staticmethod
    def dollar(amount: int) -> Money:
        from money import dollar
        return dollar.Dollar(amount)

    @staticmethod
    def franc(amount: int) -> Money:
        from money import franc
        return franc.Franc(amount)
