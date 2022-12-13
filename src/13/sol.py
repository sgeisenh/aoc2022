#!/usr/bin/env python3

import operator
from enum import Enum, auto
from functools import cmp_to_key, reduce
from itertools import chain
from typing import cast, Iterable

from read_input import read_input

ValueType = int | list["ValueType"]


def parse_value(elem: str) -> ValueType:
    return cast(ValueType, eval(elem))


def process_input(inp: str) -> list[tuple[ValueType, ValueType]]:
    entries = inp.strip().split("\n\n")
    result = []
    for entry in entries:
        left, right = map(parse_value, entry.splitlines())
        result.append((left, right))
    return result


class Compare(Enum):
    LESS = auto()
    EQUAL = auto()
    GREATER = auto()


def compare(left: ValueType, right: ValueType) -> Compare:
    match left, right:
        case int(left), int(right):
            if left < right:
                return Compare.LESS
            elif left == right:
                return Compare.EQUAL
            else:
                return Compare.GREATER
        case int(left), _:
            return compare([left], right)
        case _, int(right):
            return compare(left, [right])
        case list(left), list(right):
            for idx in range(len(left)):
                left_elem = left[idx]
                try:
                    right_elem = right[idx]
                except Exception:
                    return Compare.GREATER
                intermediate = compare(left_elem, right_elem)
                if intermediate != Compare.EQUAL:
                    return intermediate
            return compare(len(left), len(right))

    raise ValueError("Unreachable!")


def cmp(left: ValueType, right: ValueType) -> int:
    match compare(left, right):
        case Compare.LESS:
            return -1
        case Compare.EQUAL:
            return 0
        case Compare.GREATER:
            return 1

    raise ValueError("Unreachable!")


def part_one(pairs: Iterable[tuple[ValueType, ValueType]]) -> int:
    return sum(
        idx + 1 for idx, pair in enumerate(pairs) if compare(*pair) == Compare.LESS
    )


def part_two(pairs: Iterable[tuple[ValueType, ValueType]]) -> int:
    dividers: list[ValueType] = [[[2]], [[6]]]

    return reduce(
        operator.mul,
        (
            idx + 1
            for idx, value in enumerate(
                sorted(chain(*pairs, dividers), key=cmp_to_key(cmp))
            )
            if value in dividers
        ),
    )


def main() -> int:
    pairs = process_input(read_input())
    print(f"Part one: {part_one(pairs)}")
    print(f"Part two: {part_two(pairs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
