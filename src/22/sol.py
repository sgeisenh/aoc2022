from dataclasses import dataclass
from itertools import takewhile
from typing import Final
from read_input import read_input


@dataclass
class Map:
    tiles: list[str]
    path: str


def process_input(input: str) -> Map:
    tile_part, path_part = input.split("\n\n")
    return Map(tile_part.splitlines(), path_part.strip())


def turn(rot: str, direction: str) -> str:
    match rot:
        case "R":
            match direction:
                case ">":
                    return "v"
                case "v":
                    return "<"
                case "<":
                    return "^"
                case "^":
                    return ">"
                case _:
                    raise ValueError(f"Unrecognized direction: {direction}")
        case "L":
            match direction:
                case ">":
                    return "^"
                case "v":
                    return ">"
                case "<":
                    return "v"
                case "^":
                    return "<"
                case _:
                    raise ValueError(f"Unrecognized direction: {direction}")
        case _:
            raise ValueError(f"Unrecognized rot: {rot}")


DD: Final[dict[str, tuple[int, int]]] = {
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
    "^": (-1, 0),
}


def part_one(map: Map) -> int:
    row = 0
    col = map.tiles[0].index(".")
    direction = ">"
    path = map.path
    while path:
        if not path[0].isdigit():
            direction = turn(path[0], direction)
            path = path[1:]
            continue
        number_part = "".join(takewhile(lambda d: d.isdigit(), path))
        path = path[len(number_part) :]
        steps = int(number_part)
        drow, dcol = DD[direction]
        for _ in range(steps):
            nrow, ncol = row + drow, col + dcol
            if (direction == "^" or direction == "v") and (
                nrow < 0
                or nrow >= len(map.tiles)
                or ncol >= len(map.tiles[nrow])
                or map.tiles[nrow][ncol] == " "
            ):
                it = enumerate(map.tiles)
                if direction == "^":
                    it = reversed(list(it))
                for idx, r in it:
                    if ncol >= len(r):
                        continue
                    if r[ncol] == "#":
                        nrow = row
                        break
                    if r[ncol] == ".":
                        nrow = idx
                        break
            elif (
                ncol < 0 or ncol >= len(map.tiles[nrow]) or map.tiles[nrow][ncol] == " "
            ):
                it = enumerate(map.tiles[nrow])
                if direction == "<":
                    it = reversed(list(it))
                for idx, c in it:
                    if c == "#":
                        ncol = col
                        break
                    if c == ".":
                        ncol = idx
                        break
            elif map.tiles[nrow][ncol] == "#":
                nrow, ncol = row, col
            row, col = nrow, ncol

    dir_points = {">": 0, "v": 1, "<": 2, "^": 3}
    result = (row + 1) * 1000 + (col + 1) * 4 + dir_points[direction]
    return result


def get_side(row: int, col: int) -> int:
    if 0 <= row < 50:
        if 50 <= col < 100:
            return 1
        if 100 <= col < 150:
            return 2
    if 50 <= row < 100:
        if 50 <= col < 100:
            return 3
    if 100 <= row < 150:
        if 0 <= col < 50:
            return 5
        if 50 <= col < 100:
            return 4
    if 150 <= row < 200:
        if 0 <= col < 50:
            return 6
    raise ValueError(f"Unknown side for row {row} col {col}")


def jump(
    row: int, col: int, nrow: int, ncol: int, direction: str
) -> tuple[int, int, str]:
    side = get_side(row, col)
    if side == 1 and direction == "<":
        nrow = 149 - nrow
        ncol = 0
        ndir = ">"
        assert get_side(nrow, ncol) == 5
        return nrow, ncol, ndir
    if side == 5 and direction == "<":
        nrow = 149 - nrow
        ncol = 50
        ndir = ">"
        assert get_side(nrow, ncol) == 1
        return nrow, ncol, ndir
    if side == 1 and direction == "^":
        nrow = ncol + 100
        ncol = 0
        ndir = ">"
        assert get_side(nrow, ncol) == 6
        return nrow, ncol, ndir
    if side == 6 and direction == "<":
        ncol = nrow - 100
        nrow = 0
        ndir = "v"
        assert get_side(nrow, ncol) == 1
        return nrow, ncol, ndir
    if side == 2 and direction == "v":
        nrow = ncol - 50
        ncol = 99
        ndir = "<"
        assert get_side(nrow, ncol) == 3
        return nrow, ncol, ndir
    if side == 3 and direction == ">":
        ncol = nrow + 50
        nrow = 49
        ndir = "^"
        assert get_side(nrow, ncol) == 2
        return nrow, ncol, ndir
    if side == 2 and direction == "^":
        nrow = 199
        ncol = ncol - 100
        ndir = "^"
        assert get_side(nrow, ncol) == 6
        return nrow, ncol, ndir
    if side == 6 and direction == "v":
        nrow = 0
        ncol = ncol + 100
        ndir = "v"
        assert get_side(nrow, ncol) == 2
        return nrow, ncol, ndir
    if side == 2 and direction == ">":
        nrow = 149 - nrow
        ncol = 99
        ndir = "<"
        assert get_side(nrow, ncol) == 4
        return nrow, ncol, ndir
    if side == 4 and direction == ">":
        nrow = 149 - nrow
        ncol = 149
        ndir = "<"
        assert get_side(nrow, ncol) == 2
        return nrow, ncol, ndir
    if side == 3 and direction == "<":
        ncol = nrow - 50
        nrow = 100
        ndir = "v"
        assert get_side(nrow, ncol) == 5
        return nrow, ncol, ndir
    if side == 5 and direction == "^":
        nrow = ncol + 50
        ncol = 50
        ndir = ">"
        assert get_side(nrow, ncol) == 3
        return nrow, ncol, ndir
    if side == 4 and direction == "v":
        nrow = ncol + 100
        ncol = 49
        ndir = "<"
        assert get_side(nrow, ncol) == 6
        return nrow, ncol, ndir
    if side == 6 and direction == ">":
        ncol = nrow - 100
        nrow = 149
        ndir = "^"
        assert get_side(nrow, ncol) == 4
        return nrow, ncol, ndir
    raise ValueError("Unknown side dir combo")


def part_two(map: Map) -> int:
    row = 0
    col = map.tiles[0].index(".")
    direction = ">"
    path = map.path

    while path:
        if not path[0].isdigit():
            direction = turn(path[0], direction)
            path = path[1:]
            continue
        number_part = "".join(takewhile(lambda d: d.isdigit(), path))
        path = path[len(number_part) :]
        steps = int(number_part)
        for _ in range(steps):
            drow, dcol = DD[direction]
            nrow, ncol = row + drow, col + dcol
            if (
                nrow < 0
                or nrow >= len(map.tiles)
                or ncol < 0
                or ncol >= len(map.tiles[nrow])
                or map.tiles[nrow][ncol] == " "
            ):
                nrow, ncol, ndir = jump(row, col, nrow, ncol, direction)
                if map.tiles[nrow][ncol] != "#":
                    direction = ndir
                else:
                    nrow, ncol = row, col
            if map.tiles[nrow][ncol] != "#":
                row, col = nrow, ncol

    dir_points = {">": 0, "v": 1, "<": 2, "^": 3}
    result = (row + 1) * 1000 + (col + 1) * 4 + dir_points[direction]
    return result


def main() -> int:
    map = process_input(read_input())
    print(f"Part one: {part_one(map)}")
    print(f"Part two: {part_two(map)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
