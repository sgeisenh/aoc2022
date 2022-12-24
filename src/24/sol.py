from collections import defaultdict
from functools import cache
from heapq import heappush, heappop
from typing import Sequence

from read_input import read_input


def part_one(lines: Sequence[str]):
    @cache
    def get_blizzards(t: int):
        result = defaultdict(list)
        if t == 0:
            for row, line in enumerate(lines):
                for col, c in enumerate(line):
                    if c in "^v<>":
                        result[(row, col)].append(c)
            return result
        previous = get_blizzards(t - 1)
        for (pr, pc), directions in previous.items():
            for direction in directions:
                dr, dc = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}[
                    direction
                ]
                nr, nc = pr + dr, pc + dc
                if lines[nr][nc] == "#":
                    match direction:
                        case "^":
                            nr = len(lines) - 2
                        case "v":
                            nr = 1
                        case "<":
                            nc = len(lines[0]) - 2
                        case ">":
                            nc = 1
                    assert lines[nr][nc] != "#"
                result[(nr, nc)].append(direction)
        return result

    def dist_from_goal(r, c):
        gr = len(lines) - 1
        gc = len(lines[0]) - 2
        return gr - r + gc - c

    frontier = [(10000000, (0, 1, 0))]
    seen = {(0, 1, 0)}
    while frontier:
        _, (row, col, t) = heappop(frontier)
        blizzards = get_blizzards(t + 1)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]:
            nr, nc = row + dr, col + dc
            if nr == len(lines) - 1 and nc == len(lines[0]) - 2:
                return t + 1
            if (
                (nr, nc) in blizzards
                or (nr, nc, t + 1) in seen
                or (nr < 1 and ((nr, nc) != (0, 1)))
                or nr > len(lines) - 2
                or nc < 1
                or nc > len(lines[0]) - 2
            ):
                continue
            heappush(frontier, (dist_from_goal(nr, nc) + t + 1, (nr, nc, t + 1)))
            seen.add((nr, nc, t + 1))

    return None


def part_two(lines: Sequence[str]):
    @cache
    def get_blizzards(t: int):
        result = defaultdict(list)
        if t == 0:
            for row, line in enumerate(lines):
                for col, c in enumerate(line):
                    if c in "^v<>":
                        result[(row, col)].append(c)
            return result
        previous = get_blizzards(t - 1)
        for (pr, pc), directions in previous.items():
            for direction in directions:
                dr, dc = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}[
                    direction
                ]
                nr, nc = pr + dr, pc + dc
                if lines[nr][nc] == "#":
                    match direction:
                        case "^":
                            nr = len(lines) - 2
                        case "v":
                            nr = 1
                        case "<":
                            nc = len(lines[0]) - 2
                        case ">":
                            nc = 1
                    assert lines[nr][nc] != "#"
                result[(nr, nc)].append(direction)
        return result

    def shortest_time(start, goal, t):
        def dist_from_goal(r, c):
            gr, gc = goal
            return abs(gr - r) + abs(gc - c)

        sr, sc = start
        frontier = [(10000000, (sr, sc, t))]
        seen = {(sr, sc, t)}
        while frontier:
            _, (row, col, t) = heappop(frontier)
            blizzards = get_blizzards(t + 1)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]:
                nr, nc = row + dr, col + dc
                if (nr, nc) == goal:
                    return t + 1
                if (
                    (nr, nc) in blizzards
                    or (nr, nc, t + 1) in seen
                    or (nr < 1 and ((nr, nc) != start))
                    or (nr > len(lines) - 2 and ((nr, nc) != start))
                    or nc < 1
                    or nc > len(lines[0]) - 2
                ):
                    continue
                heappush(frontier, (dist_from_goal(nr, nc) + t + 1, (nr, nc, t + 1)))
                seen.add((nr, nc, t + 1))

    start = (0, 1)
    end = (len(lines) - 1, len(lines[0]) - 2)
    t = 0
    t = shortest_time(start, end, t)
    t = shortest_time(end, start, t)
    return shortest_time(start, end, t)


def main() -> int:
    lines = [line.strip() for line in read_input().splitlines()]
    print(f"Part one: {part_one(lines)}")
    print(f"Part two: {part_two(lines)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
