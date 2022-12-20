import operator
import re
from collections import deque
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass, fields, replace
from functools import reduce
from itertools import chain
from math import ceil
from typing import Iterable, Sequence

from read_input import read_input
from tqdm import tqdm

blueprint_template = re.compile(
    r"Blueprint (?P<id>\d+): Each ore robot costs (?P<ore>\d+) ore. Each clay robot costs (?P<clay>\d+) ore. Each obsidian robot costs (?P<ob_ore>\d+) ore and (?P<ob_clay>\d+) clay. Each geode robot costs (?P<geo_ore>\d+) ore and (?P<geo_ob>\d+) obsidian."
)


@dataclass
class Blueprint:
    id: int
    ore: int
    clay: int
    ob_ore: int
    ob_clay: int
    geo_ore: int
    geo_ob: int

    @classmethod
    def from_line(cls, line: str) -> "Blueprint":
        m = blueprint_template.match(line)
        if m is None:
            raise ValueError(f"Unable to parse line: {line}")
        return cls(**{field.name: int(m.group(field.name)) for field in fields(cls)})


def process_input(lines: Iterable[str]) -> list[Blueprint]:
    return [Blueprint.from_line(line) for line in lines]


@dataclass(frozen=True)
class State:
    time: int
    ore_bots: int = 1
    clay_bots: int = 0
    ob_bots: int = 0
    geo_bots: int = 0
    ore: int = 0
    clay: int = 0
    ob: int = 0
    geo: int = 0

    def __ge__(self, other) -> bool:
        return all(
            getattr(self, field.name) >= getattr(other, field.name)
            for field in fields(self)
        )

    def pass_time(self, blueprint: Blueprint, time: int) -> "State | None":
        if time > self.time:
            return None
        new_time = self.time - time
        max_ore = max(
            blueprint.ore, blueprint.clay, blueprint.ob_ore, blueprint.geo_ore
        ) * (new_time + 1)
        max_clay = blueprint.ob_clay * (new_time + 1)
        max_ob = blueprint.geo_ob * (new_time + 1)
        return replace(
            self,
            time=self.time - time,
            ore=min(max_ore, self.ore + self.ore_bots * time),
            clay=min(max_clay, self.clay + self.clay_bots * time),
            ob=min(max_ob, self.ob + self.ob_bots * time),
            geo=self.geo + self.geo_bots * time,
        )

    def make_ore(self, blueprint: Blueprint) -> list["State"]:
        time_to_make = max(0, ceil((blueprint.ore - self.ore) / self.ore_bots)) + 1
        result = self.pass_time(blueprint, time_to_make)
        if result is None:
            return []
        if all(
            self.ore_bots >= req
            for req in [
                blueprint.ore,
                blueprint.clay,
                blueprint.ob_ore,
                blueprint.geo_ore,
            ]
        ):
            return []
        final_result = replace(
            result,
            ore_bots=self.ore_bots + 1,
            ore=result.ore - blueprint.ore,
        )
        return [final_result]

    def make_clay(self, blueprint: Blueprint) -> list["State"]:
        time_to_make = max(0, ceil((blueprint.clay - self.ore) / self.ore_bots)) + 1
        result = self.pass_time(blueprint, time_to_make)
        if result is None:
            return []
        if self.clay_bots >= blueprint.ob_clay:
            return []
        return [
            replace(
                result,
                clay_bots=self.clay_bots + 1,
                ore=result.ore - blueprint.clay,
            )
        ]

    def make_ob(self, blueprint: Blueprint) -> list["State"]:
        if self.ore_bots == 0 or self.clay_bots == 0:
            return []
        time_to_make = (
            max(
                0,
                ceil((blueprint.ob_ore - self.ore) / self.ore_bots),
                ceil((blueprint.ob_clay - self.clay) / self.clay_bots),
            )
            + 1
        )
        result = self.pass_time(blueprint, time_to_make)
        if result is None:
            return []
        if self.ob_bots >= blueprint.geo_ob:
            return []
        return [
            replace(
                result,
                ob_bots=self.ob_bots + 1,
                ore=result.ore - blueprint.ob_ore,
                clay=result.clay - blueprint.ob_clay,
            )
        ]

    def make_geo(self, blueprint: Blueprint) -> list["State"]:
        if self.ore_bots == 0 or self.ob_bots == 0:
            return []
        time_to_make = (
            max(
                0,
                ceil((blueprint.geo_ore - self.ore) / self.ore_bots),
                ceil((blueprint.geo_ob - self.ob) / self.ob_bots),
            )
            + 1
        )
        result = self.pass_time(blueprint, time_to_make)
        if result is None:
            return []
        return [
            replace(
                result,
                geo_bots=self.geo_bots + 1,
                ore=result.ore - blueprint.geo_ore,
                ob=result.ob - blueprint.geo_ob,
            )
        ]

    def do_nothing(self, blueprint: Blueprint) -> list["State"]:
        result = self.pass_time(blueprint, self.time)
        assert result is not None
        return [result]


def max_geodes(bp: Blueprint, time: int) -> int:
    best = None
    seen = set()

    frontier = deque([State(time=time)])
    while frontier:
        state = frontier.popleft()
        seen.add(state)
        if state.time == 1:
            result = state.geo + state.geo_bots
            if best is None or result > best:
                best = result
        frontier.extend(
            new_state
            for new_state in chain(
                state.do_nothing(bp),
                state.make_ore(bp),
                state.make_clay(bp),
                state.make_ob(bp),
                state.make_geo(bp),
            )
            if new_state not in seen
        )

    assert best is not None
    return best


def part_one(blueprints: Sequence[Blueprint]):
    with ProcessPoolExecutor() as executor:
        future_to_bp = {executor.submit(max_geodes, bp, 24): bp for bp in blueprints}
        return sum(
            future_to_bp[future].id * future.result()
            for future in tqdm(as_completed(future_to_bp), total=len(blueprints))
        )


def part_two(blueprints: Sequence[Blueprint]):
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(max_geodes, bp, 32) for bp in blueprints[:3]]
        return reduce(
            operator.mul,
            (future.result() for future in tqdm(as_completed(futures), total=3)),
        )


def main() -> int:
    lines = [line.strip() for line in read_input().splitlines()]
    blueprints = process_input(lines)
    print(f"Part one: {part_one(blueprints)}")
    print(f"Part two: {part_two(blueprints)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
