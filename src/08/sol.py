from typing import Iterable

from read_input import read_input


def part_one(lines: Iterable[str]) -> int:
    grid = [list(line) for line in lines]
    visible = set()
    for i in range(len(grid)):
        row = grid[i]
        max_seen = None
        for j, tree in enumerate(row):
            if max_seen is None or int(tree) > max_seen:
                max_seen = int(tree)
                visible.add((i, j))
        max_seen = None
        for j, tree in reversed(list(enumerate(row))):
            if max_seen is None or int(tree) > max_seen:
                max_seen = int(tree)
                visible.add((i, j))

    for j in range(len(grid[0])):
        max_seen = None
        for i in range(len(grid)):
            tree = grid[i][j]
            if max_seen is None or int(tree) > max_seen:
                max_seen = int(tree)
                visible.add((i, j))
        max_seen = None
        for i in reversed(list(range(len(grid)))):
            tree = grid[i][j]
            if max_seen is None or int(tree) > max_seen:
                max_seen = int(tree)
                visible.add((i, j))
    return len(visible)


def part_two(lines: Iterable[str]) -> int:
    grid = [list(map(int, line)) for line in lines]

    def get_scenic_score(i, j):
        tree = grid[i][j]
        left = 0
        for lj in range(j - 1, -1, -1):
            left += 1
            if grid[i][lj] >= tree:
                break
        right = 0
        for rj in range(j + 1, len(grid[i])):
            right += 1
            if grid[i][rj] >= tree:
                break
        up = 0
        for ui in range(i - 1, -1, -1):
            up += 1
            if grid[ui][j] >= tree:
                break
        down = 0
        for di in range(i + 1, len(grid)):
            down += 1
            if grid[di][j] >= tree:
                break
        result = left * right * up * down
        return result

    best = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            score = get_scenic_score(i, j)
            if best is None or score > best:
                best = score
    assert best is not None
    return best


def main() -> int:
    lines = [line.strip() for line in read_input().splitlines()]
    print(f"Part one: {part_one(lines)}")
    print(f"Part two: {part_two(lines)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
