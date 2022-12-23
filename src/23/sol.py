from collections import defaultdict, deque
from typing import Final, Iterable

from read_input import read_input

DD: Final[dict[str, tuple[list[tuple[int, int]], tuple[int, int]]]] = {
    "N": ([(-1, -1), (-1, 0), (-1, 1)], (-1, 0)),
    "S": ([(1, -1), (1, 0), (1, 1)], (1, 0)),
    "W": ([(-1, -1), (0, -1), (1, -1)], (0, -1)),
    "E": ([(-1, 1), (0, 1), (1, 1)], (0, 1)),
}

ADJ: Final[list[tuple[int, int]]] = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def part_one(lines: Iterable[str]):
    directions = deque(["N", "S", "W", "E"])
    positions = set()
    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            if c == "#":
                positions.add((row, col))

    for _ in range(10):
        potential = defaultdict(list)
        unmoving = []
        for row, col in positions:
            if not any((row + cr, col + cc) in positions for cr, cc in ADJ):
                unmoving.append((row, col))
                continue
            for direction in directions:
                to_check, (dr, dc) = DD[direction]
                if not any((row + cr, col + cc) in positions for cr, cc in to_check):
                    potential[(row + dr, col + dc)].append((row, col))
                    break
            else:
                unmoving.append((row, col))

        new_positions = set()
        for new_pos, orig in potential.items():
            if len(orig) == 1:
                new_positions.add(new_pos)
            else:
                for pos in orig:
                    new_positions.add(pos)
        for pos in unmoving:
            new_positions.add(pos)
        positions = new_positions
        direction = directions.popleft()
        directions.append(direction)

    minrow = min(positions, key=lambda x: x[0])[0]
    maxrow = max(positions, key=lambda x: x[0])[0]
    mincol = min(positions, key=lambda x: x[1])[1]
    maxcol = max(positions, key=lambda x: x[1])[1]

    return (maxrow - minrow + 1) * (maxcol - mincol + 1) - len(positions)


def part_two(lines: Iterable[str]):
    directions = deque(["N", "S", "W", "E"])
    positions = set()
    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            if c == "#":
                positions.add((row, col))

    for round in range(1000):
        potential = defaultdict(list)
        unmoving = []
        for row, col in positions:
            if not any((row + cr, col + cc) in positions for cr, cc in ADJ):
                unmoving.append((row, col))
                continue
            for direction in directions:
                to_check, (dr, dc) = DD[direction]
                if not any((row + cr, col + cc) in positions for cr, cc in to_check):
                    potential[(row + dr, col + dc)].append((row, col))
                    break
            else:
                unmoving.append((row, col))

        moved = False
        new_positions = set()
        for new_pos, orig in potential.items():
            if len(orig) == 1:
                moved = True
                new_positions.add(new_pos)
            else:
                for pos in orig:
                    new_positions.add(pos)
        for pos in unmoving:
            new_positions.add(pos)
        if not moved:
            return round + 1
        positions = new_positions
        direction = directions.popleft()
        directions.append(direction)

    raise ValueError("WAT")


def main() -> int:
    lines = [line.strip() for line in read_input().splitlines()]
    print(f"Part one: {part_one(lines)}")
    print(f"Part two: {part_two(lines)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
