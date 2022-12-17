from collections import defaultdict
from itertools import cycle
from typing import Iterable

from read_input import read_input


def create_hor(h: int) -> list[tuple[int, int]]:
    return [(x, h + 4) for x in range(2, 6)]


def create_cross(h: int) -> list[tuple[int, int]]:
    return [(3, h + 4), *((x, h + 5) for x in range(2, 5)), (3, h + 6)]


def create_l(h: int) -> list[tuple[int, int]]:
    return [*((x, h + 4) for x in range(2, 5)), (4, h + 5), (4, h + 6)]


def create_ver(h: int) -> list[tuple[int, int]]:
    return [(2, y) for y in range(h + 4, h + 8)]


def create_box(h: int) -> list[tuple[int, int]]:
    return [(2, h + 4), (3, h + 4), (2, h + 5), (3, h + 5)]


class Settled(Exception):
    pass


def part_one(jets: str):
    jets = cycle(jets)
    shapes = cycle([create_hor, create_cross, create_l, create_ver, create_box])

    total_rocks = 0
    occupied = set()
    highest = 0

    def push(shape: list[tuple[int, int]], to: int) -> list[tuple[int, int]]:
        attempt = [(x + to, y) for x, y in shape]
        if any(x < 0 or x > 6 or (x, y) in occupied for x, y in attempt):
            return shape
        return attempt

    def drop(shape: list[tuple[int, int]]) -> list[tuple[int, int]]:
        attempt = [(x, y - 1) for x, y in shape]
        if any((x, y) in occupied or y < 1 for x, y in attempt):
            raise Settled
        return attempt

    while total_rocks < 2022:
        shape = next(shapes)(highest)
        while True:
            match next(jets):
                case ">":
                    shape = push(shape, 1)
                case "<":
                    shape = push(shape, -1)
                case _:
                    raise ValueError("Unknown jet!")
            try:
                shape = drop(shape)
            except Settled:
                break
        for x, y in shape:
            occupied.add((x, y))
            highest = max(y, highest)

        total_rocks += 1

    return max(y for _, y in occupied)


def part_two(jets: str):
    jets = cycle(enumerate(jets))
    shapes = cycle(
        enumerate([create_hor, create_cross, create_l, create_ver, create_box])
    )

    total_rocks = 0
    occupied = set()
    highest = 0
    highest_list = []

    def push(shape: list[tuple[int, int]], to: int) -> list[tuple[int, int]]:
        attempt = [(x + to, y) for x, y in shape]
        if any(x < 0 or x > 6 or (x, y) in occupied for x, y in attempt):
            return shape
        return attempt

    def drop(shape: list[tuple[int, int]]) -> list[tuple[int, int]]:
        attempt = [(x, y - 1) for x, y in shape]
        if any((x, y) in occupied or y < 1 for x, y in attempt):
            raise Settled
        return attempt

    fresh_combos = defaultdict(list)

    while total_rocks < 2022:
        sdx, shape_const = next(shapes)
        shape = shape_const(highest)
        fresh = True
        while True:
            jdx, jet = next(jets)
            if fresh:
                fresh_combos[(sdx, jdx)].append((highest, total_rocks))
            fresh = False
            match jet:
                case ">":
                    shape = push(shape, 1)
                case "<":
                    shape = push(shape, -1)
                case _:
                    raise ValueError("Unknown jet!")
            try:
                shape = drop(shape)
            except Settled:
                break
        for x, y in shape:
            occupied.add((x, y))
            if y > highest:
                highest = y
        highest_list.append(highest)

        total_rocks += 1

    period = [val for val in fresh_combos.values() if len(val) > 1][30]
    ph, pt = period[0]
    h, t = period[1]
    dh, dt = h - ph, t - pt

    rocks = 1000000000000
    to_fill = rocks - pt
    rounds = to_fill // dt
    left = to_fill % dt
    from_initial = ph
    from_rounds = dh * rounds
    from_left = highest_list[pt - 1 + left] - highest_list[pt - 1]

    return from_initial + from_rounds + from_left


def main() -> int:
    jets = read_input().strip()
    print(f"Part one: {part_one(jets)}")
    print(f"Part two: {part_two(jets)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
