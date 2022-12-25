import math
from typing import Final, Iterable

from read_input import read_input


DIGITS: Final[dict[str, int]] = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2,
}

REVERSE: Final[dict[int, str]] = {num: c for c, num in DIGITS.items()}


def max_of_digits(digits: int) -> int:
    total = 0
    for _ in range(digits):
        total = 5 * total + 2
    return total


def min_of_digits(digits: int) -> int:
    total = 0
    for _ in range(digits):
        total = 5 * total - 2
    return total


def snafu_to_int(snafu: str) -> int:
    number = 0
    for c in snafu:
        number = 5 * number + DIGITS[c]
    return number


def int_to_snafu(num: int) -> str:
    digits = math.floor(math.log(num, 5))
    while max_of_digits(digits) < num:
        digits += 1

    snafu = ""
    for curr in range(digits, 0, -1):
        for poss in range(-2, 3):
            new_num = num - poss * 5 ** (curr - 1)
            if new_num <= max_of_digits(curr - 1) and new_num >= min_of_digits(
                curr - 1
            ):
                snafu += REVERSE[poss]
                num = new_num
                break

    return snafu


def part_one(lines: Iterable[str]) -> str:
    return int_to_snafu(sum(snafu_to_int(line) for line in lines))


def main() -> int:
    lines = [line.strip() for line in read_input().splitlines()]
    print(f"Part one: {part_one(lines)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
