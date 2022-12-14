from collections import defaultdict
from typing import Iterable

from read_input import read_input


class Cave:
    def __init__(self) -> None:
        # Segment trees might be faster than lists here for very large inputs.
        # Should not matter for the AoC input size.
        self._horizontal: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
        self._vertical: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)

    def insert(self, x1: int, y1: int, x2: int, y2: int) -> None:
        if x1 == x2:
            start = min(y1, y2)
            end = max(y1, y2)
            self._vertical[x1].append((start, end))
        elif y1 == y2:
            start = min(x1, x2)
            end = max(x1, x2)
            self._horizontal[y1].append((start, end))
        else:
            raise ValueError("Unreachable")

    def lowest(self) -> int:
        hor = max(self._horizontal)
        vert = max(end for segments in self._vertical.values() for _, end in segments)
        return max(hor, vert)

    def query(self, x: int, y: int, floor: int | None = None) -> bool:
        if floor is not None and y >= floor:
            return True
        if x in self._vertical:
            for y1, y2 in self._vertical[x]:
                if y1 <= y <= y2:
                    return True
        if y in self._horizontal:
            for x1, x2 in self._horizontal[y]:
                if x1 <= x <= x2:
                    return True
        return False


def process_input(lines: Iterable[str]) -> Cave:
    result = Cave()
    for line in lines:
        points = line.split(" -> ")
        for origin, end in zip(points[:-1], points[1:]):
            x1, y1 = map(int, origin.split(","))
            x2, y2 = map(int, end.split(","))
            result.insert(x1, y1, x2, y2)
    return result


def part_one(cave: Cave) -> int:
    lowest = cave.lowest()
    sand = set()

    while True:
        at_rest = False
        x, y = 500, 0
        while y < lowest and not at_rest:
            to_try = [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]
            for nx, ny in to_try:
                if not cave.query(nx, ny) and (nx, ny) not in sand:
                    break
            else:
                at_rest = True
            if not at_rest:
                x, y = nx, ny
        if at_rest:
            sand.add((x, y))
        else:
            return len(sand)


def part_two(cave: Cave) -> int:
    sand = set()
    floor = cave.lowest() + 2

    while True:
        if (500, 0) in sand:
            return len(sand)
        x, y = 500, 0
        while True:
            to_try = [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]
            for nx, ny in to_try:
                if not cave.query(nx, ny, floor=floor) and (nx, ny) not in sand:
                    break
            else:
                break
            x, y = nx, ny
        sand.add((x, y))


def main() -> int:
    lines = [line.strip() for line in read_input().splitlines()]
    cave = process_input(lines)
    print(f"Part one: {part_one(cave)}")
    print(f"Part two: {part_two(cave)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
