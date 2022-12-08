from typing import Iterable

from read_input import read_input


def part_one(lines: Iterable[str]) -> int:
    scores = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6,
    }
    return sum(scores[line] for line in lines)


def part_two(lines: Iterable[str]) -> int:
    scores = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7,
    }
    return sum(scores[line] for line in lines)


def main() -> int:
    input = read_input().splitlines()
    print(f"Part one: {part_one(input)}")
    print(f"Part two: {part_two(input)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
