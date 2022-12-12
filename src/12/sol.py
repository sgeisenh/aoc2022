from collections import deque
from typing import Deque, Iterable, Sequence

from read_input import read_input


def process_input(input: str) -> list[list[str]]:
    return [list(line.strip()) for line in input.strip().splitlines()]


def bfs(grid: Sequence[Sequence[str]], starts: Iterable[tuple[int, int]]) -> int | None:
    seen = set(starts)
    frontier: Deque[tuple[int, int, int]] = deque((r, c, 0) for r, c in seen)

    while frontier:
        r, c, steps = frontier.popleft()
        val = grid[r][c]
        val = ord(val) if val != "S" else ord("a")
        for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
            nr = r + dr
            nc = c + dc
            if (
                nr < 0
                or nr >= len(grid)
                or nc < 0
                or nc >= len(grid[0])
                or (nr, nc) in seen
            ):
                continue
            nv = grid[nr][nc]
            match nv:
                case "S":
                    no = ord("a")
                case "E":
                    no = ord("z")
                case _:
                    no = ord(nv)
            if no <= val + 1:
                if nv == "E":
                    return steps + 1

                frontier.append((nr, nc, steps + 1))
                seen.add((nr, nc))


def part_one(grid: Sequence[Sequence[str]]) -> int | None:
    return bfs(
        grid,
        (
            (r, c)
            for r, row in enumerate(grid)
            for c, val in enumerate(row)
            if val == "S"
        ),
    )


def part_two(grid: Sequence[Sequence[str]]) -> int | None:
    return bfs(
        grid,
        (
            (r, c)
            for r, row in enumerate(grid)
            for c, val in enumerate(row)
            if val in "Sa"
        ),
    )


def main() -> int:
    grid = process_input(read_input())
    print(f"Part one: {part_one(grid)}")
    print(f"Part two: {part_two(grid)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
