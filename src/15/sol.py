from typing import Iterable

from read_input import read_input


def dist(x1: int, y1: int, x2: int, y2: int):
    return abs(x1 - x2) + abs(y1 - y2)


def process_input(lines: Iterable[str]) -> list[tuple[int, int, int, int]]:
    result = []
    for line in lines:
        line = line.strip()
        line = line.removeprefix("Sensor at x=")
        sx, line = line.split(", ", 1)
        sx = int(sx)
        line = line.removeprefix("y=")
        sy, line = line.split(": ", 1)
        sy = int(sy)
        line = line.removeprefix("closest beacon is at x=")
        bx, line = line.split(", ")
        bx = int(bx)
        by = int(line.removeprefix("y="))
        result.append((sx, sy, bx, by))
    return result


def part_one(pairs: Iterable[tuple[int, int, int, int]]) -> int:
    row = 2000000
    intervals = []
    for sx, sy, bx, by in pairs:
        d = dist(sx, sy, bx, by)
        slack = d - abs(sy - row)
        if slack < 0:
            continue
        intervals.append((sx - slack, sx + slack))
    intervals.sort(key=lambda x: x[0])
    total = 0
    pr = intervals[0][0]
    for left, right in intervals:
        if left > pr:
            total += right - left + 1
        elif right > pr:
            total += right - pr
        pr = max(pr, right)
    return total


def part_two(pairs: Iterable[tuple[int, int, int, int]]):
    with_distances = []

    for sx, sy, bx, by in pairs:
        mandist = dist(sx, sy, bx, by)
        with_distances.append((sx, sy, mandist))

    for y in range(0, 4000001):
        intervals = []
        for sx, sy, md in with_distances:
            yd = abs(y - sy)
            slack = md - yd
            if slack < 0:
                continue
            intervals.append((sx - slack, sx + slack))
        intervals.sort(key=lambda x: x[0])
        pr = intervals[0][0]
        if pr > 0:
            return y
        for left, right in intervals:
            if left > pr + 1:
                return 4000000 * (pr + 1) + y
            pr = max(pr, right)
        if pr < 4000000:
            return 4000000 * (pr + 1) + y


def main() -> int:
    lines = [line.strip() for line in read_input().splitlines()]
    pairs = process_input(lines)
    print(f"Part one: {part_one(pairs)}")
    print(f"Part two: {part_two(pairs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
