from typing import Iterable

from read_input import read_input


def part_one(lines: Iterable[str]):
    return 0


def part_two(lines: Iterable[str]):
    return 0


def main() -> int:
    lines = [line.strip() for line in read_input().splitlines()]
    print(f"Part one: {part_one(lines)}")
    print(f"Part two: {part_two(lines)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
