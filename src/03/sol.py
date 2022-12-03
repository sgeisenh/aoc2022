import fileinput
import operator
from functools import reduce

lines = [line.strip() for line in fileinput.input()]


def item_to_priority(item):
    if "a" <= item <= "z":
        return ord(item) - ord("a") + 1
    else:
        return ord(item) - ord("A") + 27


p1 = sum(
    item_to_priority(
        next(iter(set(line[: len(line) // 2]) & set(line[len(line) // 2 :])))
    )
    for line in lines
)
print("Part one:", p1)

p2 = sum(
    item_to_priority(next(iter(reduce(operator.and_, map(set, lines[idx : idx + 3])))))
    for idx in range(0, len(lines), 3)
)
print("Part two:", p2)
