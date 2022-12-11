from collections import deque
from dataclasses import dataclass
from heapq import nlargest
from typing import Callable, Iterable

from read_input import read_input


@dataclass
class Monkey:
    id: int
    starting: list[int]
    operation: Callable[[int], int]
    divisor: int
    yes: int
    no: int


def parse_op(op_line: str) -> Callable[[int], int]:
    op_line = op_line.strip().removeprefix("Operation: new = ")
    left, op, right = op_line.split()

    def operation(old: int) -> int:
        if left == "old":
            l = old
        else:
            l = int(left)
        if right == "old":
            r = old
        else:
            r = int(right)
        if op == "+":
            return l + r
        elif op == "*":
            return l * r
        else:
            raise ValueError("Unrecognized op")

    return operation


def parse_input(input: str) -> list[Monkey]:
    entries = input.split("\n\n")
    results = []
    for entry in entries:
        id_line, starting, operation, test, yes, no = entry.splitlines()
        monkey_id = int(id_line.strip().removeprefix("Monkey ").removesuffix(":"))
        starting = list(
            map(int, starting.strip().removeprefix("Starting items: ").split(", "))
        )
        operation = parse_op(operation)
        divisor = int(test.strip().removeprefix("Test: divisible by "))
        yes = int(yes.strip().removeprefix("If true: throw to monkey "))
        no = int(no.strip().removeprefix("If false: throw to monkey "))
        results.append(Monkey(monkey_id, starting, operation, divisor, yes, no))
    return results


def part_one(monkeys: list[Monkey]) -> int:
    num_inspected = [0 for _ in monkeys]
    current_items = [list(monkey.starting) for monkey in monkeys]

    for _ in range(20):
        for idx, monkey in enumerate(monkeys):
            for item in current_items[idx]:
                num_inspected[idx] += 1
                item = monkey.operation(item)
                item = item // 3
                if item % monkey.divisor == 0:
                    current_items[monkey.yes].append(item)
                else:
                    current_items[monkey.no].append(item)
            current_items[idx] = []

    x, y = nlargest(2, num_inspected)
    return x * y


def part_two(monkeys: list[Monkey]):
    num_inspected = [0 for _ in monkeys]
    current_items = [list(monkey.starting) for monkey in monkeys]

    multiple = 1
    for monkey in monkeys:
        multiple *= monkey.divisor

    for _ in range(10000):
        for idx, monkey in enumerate(monkeys):
            for item in current_items[idx]:
                num_inspected[idx] += 1
                item = monkey.operation(item) % multiple
                if item % monkey.divisor == 0:
                    current_items[monkey.yes].append(item)
                else:
                    current_items[monkey.no].append(item)
            current_items[idx] = []

    x, y = nlargest(2, num_inspected)
    return x * y


def main() -> int:
    input = read_input()
    monkeys = parse_input(input)
    print(f"Part one: {part_one(monkeys)}")
    print(f"Part two: {part_two(monkeys)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
