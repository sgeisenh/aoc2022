import heapq
from typing import Iterable

from read_input import read_input


def process_input(input: str) -> list[int]:
    return heapq.nlargest(
        3,
        (
            sum(map(int, section.strip().splitlines()))
            for section in input.split("\n\n")
        ),
    )


def part_one(top_three: Iterable[int]) -> int:
    return max(top_three)


def part_two(top_three: Iterable[int]) -> int:
    return sum(top_three)


def main() -> int:
    input = read_input()
    top_three = process_input(input)
    print(f"Part one: {part_one(top_three)}")
    print(f"Part two: {part_two(top_three)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
