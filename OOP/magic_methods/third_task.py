# Description
# Implement class Currency and inherited classes Euro, Dollar, Pound. Course is 1 EUR == 2 USD == 100 GBP
#
# You need to implement the following methods:
#
# course - classmethod which returns string in the following pattern: {float value} {currency to} for 1 {currency for}
# to_currency - method transforms currency from one currency to another.
# Method should return instance of a required currency.

from __future__ import annotations
from typing import Type, ClassVar


class Currency:
    rate_to_eur: ClassVar[float]
    code: ClassVar[str]

    """
    1 EUR = 2 USD = 100 GBP

    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """

    def __init__(self, value: float):
        self.value = value

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        x = cls.rate_to_eur / other_cls.rate_to_eur
        return f"{x} {other_cls.code} for 1 {cls.code}"

    def to_currency(self, other_cls: Type[Currency]):
        new_value = self.value * type(self).rate_to_eur / other_cls.rate_to_eur
        return other_cls(new_value)

    def __add__(self, other):
        if not isinstance(other, Currency):
            return NotImplemented

        other_converted = other.to_currency(type(self))
        sum_value = self.value + other_converted.value
        return type(self)(sum_value)

    def __str__(self):
        return f"{self.value} {self.code}"

    def __eq__(self, other):
        if not isinstance(other, Currency):
            return NotImplemented
        self_in_eur = self.value * type(self).rate_to_eur
        other_in_eur = other.value * other.rate_to_eur
        return self_in_eur == other_in_eur

    def __lt__(self, other):
        if not isinstance(other, Currency):
            return NotImplemented
        self_in_eur = self.value * type(self).rate_to_eur
        other_in_eur = other.value * other.rate_to_eur
        return self_in_eur < other_in_eur

    def __gt__(self, other):
        if not isinstance(other, Currency):
            return NotImplemented
        self_in_eur = self.value * type(self).rate_to_eur
        other_in_eur = other.value * other.rate_to_eur
        return self_in_eur > other_in_eur


class Euro(Currency):
    rate_to_eur = 1
    code = "EUR"


class Dollar(Currency):
    rate_to_eur = 0.5
    code = "USD"


class Pound(Currency):
    rate_to_eur = 0.01
    code = "GBP"


def demo():
    print(
        f"Euro.course(Pound)   ==> {Euro.course(Pound)}\n"
        f"Dollar.course(Pound) ==> {Dollar.course(Pound)}\n"
        f"Pound.course(Euro)   ==> {Pound.course(Euro)}\n"
    )

    e = Euro(100)
    r = Pound(100)
    d = Dollar(200)

    print(
        f"e = {e}\n"
        f"e.to_currency(Dollar) = {e.to_currency(Dollar)}\n"
        f"e.to_currency(Pound)  = {e.to_currency(Pound)}\n"
        f"e.to_currency(Euro)   = {e.to_currency(Euro)}\n"
    )

    print(
        f"r = {r}\n"
        f"r.to_currency(Dollar) = {r.to_currency(Dollar)}\n"
        f"r.to_currency(Euro)   = {r.to_currency(Euro)}\n"
        f"r.to_currency(Pound)  = {r.to_currency(Pound)}\n"
    )

    print(
        f"e + r => {e + r}\n"
        f"r + d => {r + d}\n"
        f"d + e => {d + e}\n"
    )

    print(Euro(1) == Dollar(2))
    print(Pound(100) == Euro(1))
    print(Dollar(1) > Pound(1))


if __name__ == "__main__":
    demo()
