import operator
from functools import reduce
from typing import Iterable

from read_input import read_input


def item_to_priority(item: str) -> int:
    if "a" <= item <= "z":
        return ord(item) - ord("a") + 1
    else:
        return ord(item) - ord("A") + 27


def part_one(lines: Iterable[str]) -> int:
    def item_from_line(line: str) -> str:
        midway = len(line) // 2
        intersection = set(line[:midway]) & set(line[midway:])
        return next(iter(intersection))

    return sum(item_to_priority(item_from_line(line)) for line in lines)


def part_two(lines: Iterable[str]) -> int:
    def item_from_chunk(chunk: Iterable[str]) -> str:
        intersection = reduce(operator.and_, map(set, chunk))
        return next(iter(intersection))

    chunks = zip(*([iter(lines)] * 3), strict=True)
    return sum(item_to_priority(item_from_chunk(chunk)) for chunk in chunks)


def main() -> int:
    lines = [line.strip() for line in read_input().splitlines()]
    print(f"Part one: {part_one(lines)}")
    print(f"Part two: {part_two(lines)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
