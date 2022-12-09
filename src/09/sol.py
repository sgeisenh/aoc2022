from typing import Iterable

from read_input import read_input


def get_new_tail(head: tuple[int, int], tail: tuple[int, int]) -> tuple[int, int]:
    hx, hy = head
    tx, ty = tail
    if abs(hx - tx) > 1:
        sign = -1 if hx < tx else 1
        tx += sign
        if hy != ty:
            sign = -1 if hy < ty else 1
            ty += sign
    elif abs(hy - ty) > 1:
        sign = -1 if hy < ty else 1
        ty += sign
        if hx != tx:
            sign = -1 if hx < tx else 1
            tx += sign
    return tx, ty


DIRECTIONS: dict[str, tuple[int, int]] = {
    "R": (1, 0),
    "U": (0, 1),
    "L": (-1, 0),
    "D": (0, -1),
}


def solve(lines: Iterable[str], knots: int) -> int:
    hx, hy = 0, 0
    tails = [(0, 0)] * (knots - 1)
    tail_set = {tails[-1]}
    for line in lines:
        direction, steps = line.split()
        dx, dy = DIRECTIONS[direction]
        for _ in range(int(steps)):
            hx += dx
            hy += dy
            px, py = hx, hy
            new_tails = []
            for tail in tails:
                tx, ty = get_new_tail((px, py), tail)
                new_tails.append((tx, ty))
                px, py = tx, ty
            tails = new_tails
            tail_set.add(tails[-1])
    return len(tail_set)


def part_one(lines: Iterable[str]) -> int:
    return solve(lines, 2)


def part_two(lines: Iterable[str]) -> int:
    return solve(lines, 10)


def main() -> int:
    lines = [line.strip() for line in read_input().splitlines()]
    print(f"Part one: {part_one(lines)}")
    print(f"Part two: {part_two(lines)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
