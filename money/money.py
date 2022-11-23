from __future__ import annotations

class Money:

    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def __eq__(self, other: Money) -> bool:
        return self.__dict__ == other.__dict__ and \
            self.__class__ == other.__class__

    def equals(self, other: Money) -> bool:
        return self._amount == other._amount and \
            self.__class__ == other.__class__

    def __str__(self) -> str:
        return f"{self._amount} {self._currency}"

    __repr__ = __str__

    def times(self, amount: int, multiplyer: int) -> Money:
        pass

    def currency(self) -> str:
        return self._currency

    @staticmethod
    def dollar(amount: int) -> Money:
        from money import dollar
        return dollar.Dollar(amount, "USD")

    @staticmethod
    def franc(amount: int) -> Money:
        from money import franc
        return franc.Franc(amount, "CHF")

if __name__ == "__main__":
    # test __str__()
    money = Money.dollar(1)
    print(money)
    print(money.times(2) == Money.dollar(2))

    money2 = Money.franc(1)
    print(money2)
    print(money2.times(2) == Money.franc(2))
