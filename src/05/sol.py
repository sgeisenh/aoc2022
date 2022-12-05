import fileinput
from copy import deepcopy

corpus = "".join(fileinput.input())
setup, procedure = corpus.split("\n\n")
setup = setup.splitlines()[:-1]

stacks = [[] for _ in range(9)]

for line in setup:
    for i in range(9):
        idx = 4 * i + 1
        if idx < len(line) and line[idx] != " ":
            stacks[i].append(line[idx])

for stack in stacks:
    stack.reverse()


def parse_line(line: str) -> tuple[int, int, int]:
    words = line.split()
    return int(words[1]), int(words[3]) - 1, int(words[5]) - 1


def move(stacks: list[list[str]], fro: int, to: int):
    item = stacks[fro].pop()
    stacks[to].append(item)


def part1(stacks: list[list[str]]) -> str:
    stacks = deepcopy(stacks)
    for line in procedure.splitlines():
        n, fro, to = parse_line(line)
        for _ in range(n):
            move(stacks, fro, to)
    return "".join(stack[-1] for stack in stacks)


def part2(stacks: list[list[str]]) -> str:
    stacks = deepcopy(stacks)
    for line in procedure.splitlines():
        n, fro, to = parse_line(line)
        stacks[fro][-n:] = list(reversed(stacks[fro][-n:]))
        for _ in range(n):
            move(stacks, fro, to)
    return "".join(stack[-1] for stack in stacks)


print(f"Part one: {part1(stacks)}")
print(f"Part two: {part2(stacks)}")
