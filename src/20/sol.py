from dataclasses import dataclass
from typing import Iterable

from read_input import read_input


def part_one(lines: Iterable[str]):
    numbers = list(map(int, lines))
    idxs = {idx: idx for idx in range(len(numbers))}
    for idx in range(len(numbers)):
        actual = idxs[idx]
        number = numbers[actual]
        new_idx = (actual + number - 1) % (len(numbers) - 1) + 1
        if new_idx > actual:
            numbers = (
                numbers[:actual]
                + numbers[actual + 1 : new_idx + 1]
                + [number]
                + numbers[new_idx + 1 :]
            )
            new_idxs = {idx: new_idx}
            for orig, now in idxs.items():
                if actual < now <= new_idx:
                    new_idxs[orig] = now - 1
                elif orig != idx:
                    new_idxs[orig] = now
            idxs = new_idxs
        elif new_idx < actual:
            numbers = (
                numbers[:new_idx]
                + [number]
                + numbers[new_idx:actual]
                + numbers[actual + 1 :]
            )
            new_idxs = {idx: new_idx}
            for orig, now in idxs.items():
                if new_idx <= now < actual:
                    new_idxs[orig] = now + 1
                elif orig != idx:
                    new_idxs[orig] = now
            idxs = new_idxs
    zero_idx = numbers.index(0)
    return sum(numbers[(zero_idx + elem) % len(numbers)] for elem in [1000, 2000, 3000])


def part_two(lines: Iterable[str]):
    key = 811589153
    numbers = [key * int(line) for line in lines]
    idxs = {idx: idx for idx in range(len(numbers))}
    for _ in range(10):
        for idx in range(len(numbers)):
            actual = idxs[idx]
            number = numbers[actual]
            new_idx = (actual + number - 1) % (len(numbers) - 1) + 1
            if new_idx > actual:
                numbers = (
                    numbers[:actual]
                    + numbers[actual + 1 : new_idx + 1]
                    + [number]
                    + numbers[new_idx + 1 :]
                )
                new_idxs = {idx: new_idx}
                for orig, now in idxs.items():
                    if actual < now <= new_idx:
                        new_idxs[orig] = now - 1
                    elif orig != idx:
                        new_idxs[orig] = now
                idxs = new_idxs
            elif new_idx < actual:
                numbers = (
                    numbers[:new_idx]
                    + [number]
                    + numbers[new_idx:actual]
                    + numbers[actual + 1 :]
                )
                new_idxs = {idx: new_idx}
                for orig, now in idxs.items():
                    if new_idx <= now < actual:
                        new_idxs[orig] = now + 1
                    elif orig != idx:
                        new_idxs[orig] = now
                idxs = new_idxs
    zero_idx = numbers.index(0)
    return sum(numbers[(zero_idx + elem) % len(numbers)] for elem in [1000, 2000, 3000])


def main() -> int:
    lines = [line.strip() for line in read_input().splitlines()]
    print(f"Part one: {part_one(lines)}")
    print(f"Part two: {part_two(lines)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
