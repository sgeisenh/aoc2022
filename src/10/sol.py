from typing import Iterable

from read_input import read_input


def part_one(lines: Iterable[str]) -> int:
    cycle = 1
    x = 1
    total = 0

    def tick() -> None:
        nonlocal cycle, total
        cycle += 1
        if cycle in {20, 60, 100, 140, 180, 220}:
            total += x * cycle

    for line in lines:
        if line.startswith("noop"):
            tick()
        else:
            tick()
            _, incr = line.split()
            x += int(incr)
            tick()

    return total


def part_two(lines: Iterable[str]) -> None:
    cycle = 0
    x = 1
    row = ["."] * 40

    def draw() -> None:
        nonlocal row
        col = cycle % 40
        if abs(x - col) <= 1:
            row[col] = "#"

    def tick() -> None:
        nonlocal cycle, row
        cycle += 1
        if cycle % 40 == 0:
            print("".join(row))
            row = ["."] * 40

    for line in lines:
        draw()
        if line.startswith("noop"):
            tick()
        else:
            _, incr = line.split()
            incr = int(incr)
            tick()
            draw()
            x += incr
            tick()


def main() -> int:
    lines = [line.strip() for line in read_input().splitlines()]
    print(f"Part one: {part_one(lines)}")
    print(f"Part two: {part_two(lines)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
