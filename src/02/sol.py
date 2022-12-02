import fileinput


def create_input() -> list[tuple[str, str]]:
    result = []
    for line in fileinput.input():
        them, me = line.strip().split()
        result.append((them, me))
    return result


def part_one(rounds: list[tuple[str, str]]) -> int:
    score = 0
    for them, me in rounds:
        match me:
            case "X":
                score += 1
                match them:
                    case "A":
                        score += 3
                    case "B":
                        score += 0
                    case "C":
                        score += 6
            case "Y":
                score += 2
                match them:
                    case "A":
                        score += 6
                    case "B":
                        score += 3
                    case "C":
                        score += 0
            case "Z":
                score += 3
                match them:
                    case "A":
                        score += 0
                    case "B":
                        score += 6
                    case "C":
                        score += 3
    return score


def part_two(rounds: list[tuple[str, str]]) -> int:
    score = 0
    for them, me in rounds:
        match me:
            case "X":
                score += 0
                match them:
                    case "A":
                        score += 3
                    case "B":
                        score += 1
                    case "C":
                        score += 2
            case "Y":
                score += 3
                match them:
                    case "A":
                        score += 1
                    case "B":
                        score += 2
                    case "C":
                        score += 3
            case "Z":
                score += 6
                match them:
                    case "A":
                        score += 2
                    case "B":
                        score += 3
                    case "C":
                        score += 1
    return score


def main() -> None:
    input = create_input()
    print(f"Part one: {part_one(input)}")
    print(f"Part two: {part_two(input)}")


if __name__ == "__main__":
    main()
