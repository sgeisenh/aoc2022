from dataclasses import dataclass
from operator import add, mul, sub, floordiv
from typing import Iterable, Callable, Mapping

from read_input import read_input


@dataclass(frozen=True)
class Binop:
    op: Callable[[int, int], int]
    left: str
    right: str


@dataclass(frozen=True)
class Lit:
    value: int


Expr = Binop | Lit


def parse_line(line: str) -> tuple[str, Expr]:
    name, rest = line.split(": ")
    tokens = rest.split()
    match tokens:
        case [num]:
            expr = Lit(int(num))
        case [left, ops, right]:
            match ops:
                case "+":
                    op = add
                case "*":
                    op = mul
                case "-":
                    op = sub
                case "/":
                    op = floordiv
                case _:
                    raise ValueError(f"Invalid operator: {ops}")
            expr = Binop(op, left, right)
        case _:
            raise ValueError(f"Invalid tokens: {tokens}")
    return (name, expr)


def process_input(lines: Iterable[str]) -> dict[str, Expr]:
    return dict(map(parse_line, lines))


def part_one(exprs: Mapping[str, Expr]) -> int:
    cache = {}

    def evaluate(var: str) -> int:
        nonlocal cache
        cached = cache.get(var)
        if cached is not None:
            return cached
        match exprs[var]:
            case Lit(value):
                return value
            case Binop(op, left, right):
                leval = evaluate(left)
                reval = evaluate(right)
                return op(leval, reval)

    return evaluate("root")


def part_two(exprs: Mapping[str, Expr]) -> int:
    cache = {}

    def evaluate(var: str) -> int:
        nonlocal cache
        cached = cache.get(var)
        if cached is not None:
            return cached
        match exprs[var]:
            case Lit(value):
                return value
            case Binop(op, left, right):
                leval = evaluate(left)
                reval = evaluate(right)
                return op(leval, reval)

    def search(var: str, acc: list[str]) -> list[str] | None:
        if var == "humn":
            return acc
        match exprs[var]:
            case Lit(_):
                return None
            case Binop(_, left, right):
                acc.append("left")
                lres = search(left, acc)
                if lres is not None:
                    return lres
                acc.pop()
                acc.append("right")
                rres = search(right, acc)
                if rres is not None:
                    return rres
                acc.pop()
                return None

    path = search("root", [])
    assert path is not None

    curr = exprs["root"]
    assert isinstance(curr, Binop)
    match path[0]:
        case "left":
            to_match = evaluate(curr.right)
            curr = exprs[curr.left]
        case "right":
            to_match = evaluate(curr.left)
            curr = exprs[curr.right]
        case _:
            raise ValueError("Unreachable")
    for direction in path[1:]:
        assert isinstance(curr, Binop), f"Wat: {curr}"
        match direction:
            case "left":
                other = evaluate(curr.right)
                if curr.op is add:
                    to_match = to_match - other
                if curr.op is mul:
                    to_match = to_match // other
                if curr.op is sub:
                    to_match = to_match + other
                if curr.op is floordiv:
                    to_match = to_match * other
                curr = exprs[curr.left]
            case "right":
                other = evaluate(curr.left)
                if curr.op is add:
                    to_match = to_match - other
                if curr.op is mul:
                    to_match = to_match // other
                if curr.op is sub:
                    to_match = other - to_match
                if curr.op is floordiv:
                    to_match = other // to_match
                curr = exprs[curr.right]

    return to_match


def main() -> int:
    lines = [line.strip() for line in read_input().splitlines()]
    exprs = process_input(lines)
    print(f"Part one: {part_one(exprs)}")
    print(f"Part two: {part_two(exprs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
