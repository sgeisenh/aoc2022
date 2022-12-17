from collections import defaultdict
from dataclasses import dataclass
from pprint import pprint
from typing import Iterable, Mapping, Sequence

from read_input import read_input


@dataclass
class Valve:
    name: str
    rate: int
    tunnels: list[str]


def process_input(lines: Iterable[str]) -> list[Valve]:
    result = []
    for line in lines:
        words = line.split()
        name = words[1]
        rate = int(words[4].removeprefix("rate=").strip(";"))
        if "lead to valves " in line:
            _, _, suffix = line.partition("lead to valves ")
        else:
            _, _, suffix = line.partition("leads to valve ")
        tunnels = suffix.split(", ")
        result.append(Valve(name, rate, tunnels))
    return result


def shortest_paths(valves: Sequence[Valve]) -> dict[str, dict[str, int | None]]:
    result = {
        valve.name: {
            other.name: 0 if valve.name == other.name else None for other in valves
        }
        for valve in valves
    }
    for valve in valves:
        for tunnel in valve.tunnels:
            result[valve.name][tunnel] = 1
    names = [valve.name for valve in valves]
    for k in names:
        for i in names:
            snd = result[i][k]
            if snd is None:
                continue
            for j in names:
                thd = result[k][j]
                if thd is None:
                    continue
                fst = result[i][j]
                combined = snd + thd
                if fst is None or fst > combined:
                    result[i][j] = combined
    return result


def create_sol(
    starting_time: int,
    valves: Sequence[Valve],
) -> dict[frozenset[str], int]:
    dists = shortest_paths(valves)
    rates = {valve.name: valve.rate for valve in valves if valve.rate > 0}

    sol = {}

    def populate_sol(time: int, location: str, open: frozenset[str], flow: int) -> int:
        nonlocal sol
        sol[open] = max(sol.get(open, 0), flow)
        if time <= 0:
            return 0

        for poss in rates:
            dist = dists[location][poss]
            new_time = time - dist - 1
            if poss in open or new_time < 0:
                continue
            populate_sol(
                new_time, poss, open | frozenset([poss]), flow + new_time * rates[poss]
            )

    populate_sol(starting_time, "AA", frozenset(), 0)
    return sol


def part_one(valves: Sequence[Valve]) -> int:
    sol = create_sol(30, valves)
    return max(sol.values())


def part_two(
    valves: Sequence[Valve],
) -> int:
    sol = create_sol(26, valves)
    return max(
        v1 + v2 for k1, v1 in sol.items() for k2, v2 in sol.items() if not k1 & k2
    )


def main() -> int:
    lines = [line.strip() for line in read_input().splitlines()]
    valves = process_input(lines)
    print(f"Part one: {part_one(valves)}")
    print(f"Part two: {part_two(valves)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
