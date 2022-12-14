from collections import defaultdict
from typing import Iterable

from read_input import read_input


def sign(x: int) -> int:
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1


Cave = set[tuple[int, int]]


def process_input(lines: Iterable[str]) -> Cave:
    result = set()
    for line in lines:
        points = line.split(" -> ")
        for origin, end in zip(points[:-1], points[1:]):
            x1, y1 = map(int, origin.split(","))
            x2, y2 = map(int, end.split(","))
            dx = sign(x2 - x1)
            dy = sign(y2 - y1)

            x, y = x1, y1
            while x != x2 or y != y2:
                result.add((x, y))
                x += dx
                y += dy
            result.add((x, y))
    return result


def part_one(cave: Cave) -> int:
    occupied = set(cave)
    lowest = max(y for _, y in occupied)

    while True:
        x, y = 500, 0
        while y < lowest:
            ny = y + 1
            for nx in [x, x - 1, x + 1]:
                if (nx, ny) not in occupied:
                    break
            else:
                break
            x, y = nx, ny
        else:
            return len(occupied) - len(cave)
        occupied.add((x, y))


def part_two(cave: Cave) -> int:
    occupied = set(cave)
    floor = max(y for _, y in occupied) + 2

    while True:
        if (500, 0) in occupied:
            return len(occupied) - len(cave)
        x, y = 500, 0
        while True:
            ny = y + 1
            for nx in [x, x - 1, x + 1]:
                if (nx, ny) not in occupied and ny < floor:
                    break
            else:
                break
            x, y = nx, ny
        occupied.add((x, y))


def main() -> int:
    lines = [line.strip() for line in read_input().splitlines()]
    cave = process_input(lines)
    print(f"Part one: {part_one(cave)}")
    print(f"Part two: {part_two(cave)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
