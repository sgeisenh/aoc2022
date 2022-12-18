from collections import defaultdict, deque
from itertools import chain
from typing import AbstractSet, Iterable

from read_input import read_input


def parse_line(line: str) -> tuple[int, int, int]:
    x, y, z = map(int, line.split(","))
    return x, y, z


def process_input(lines: Iterable[str]) -> set[tuple[int, int, int]]:
    return {parse_line(line) for line in lines}


def part_one(cubes: AbstractSet[tuple[int, int, int]]) -> int:
    total = 0
    for x, y, z in cubes:
        for dx, dy, dz in [
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        ]:
            if (x + dx, y + dy, z + dz) not in cubes:
                total += 1
    return total


SURROUNDING = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
]


def part_two(cubes: AbstractSet[tuple[int, int, int]]) -> int:
    air_cubes = defaultdict(int)
    for x, y, z in cubes:
        for dx, dy, dz in SURROUNDING:
            nc = x + dx, y + dy, z + dz
            if nc not in cubes:
                air_cubes[nc] += 1
    internal = set()
    external = set()

    def bfs(start: tuple[int, int, int]):
        nonlocal internal, external
        if start in internal or start in external:
            return

        frontier = {start}
        seen = {start}
        for _ in range(20):
            new_frontier = set()
            if not frontier:
                for loc in seen:
                    internal.add(loc)
                return
            for (x, y, z) in frontier:
                seen.add((x, y, z))
                for dx, dy, dz in SURROUNDING:
                    nc = x + dx, y + dy, z + dz
                    if nc in internal:
                        for loc in seen:
                            internal.add(loc)
                        return
                    if nc in external:
                        for loc in seen:
                            external.add(loc)
                        return
                    if nc not in seen and nc not in cubes:
                        new_frontier.add(nc)
            frontier = new_frontier

    for loc in air_cubes:
        bfs(loc)

    total = 0
    for loc, count in air_cubes.items():
        if loc not in internal:
            total += count

    return total


def main() -> int:
    lines = [line.strip() for line in read_input().splitlines()]
    cubes = process_input(lines)
    print(f"Part one: {part_one(cubes)}")
    print(f"Part two: {part_two(cubes)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
