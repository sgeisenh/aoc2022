fn process_input(input: &str) -> Vec<&str> {
    input.lines().map(str::trim).collect()
}

fn part1(rounds: &[&str]) -> i32 {
    fn score(round: &str) -> i32 {
        match round {
            "A X" => 3 + 1,
            "A Y" => 6 + 2,
            "A Z" => 0 + 3,
            "B X" => 0 + 1,
            "B Y" => 3 + 2,
            "B Z" => 6 + 3,
            "C X" => 6 + 1,
            "C Y" => 0 + 2,
            "C Z" => 3 + 3,
            _ => panic!("Impossible round {}", round),
        }
    }
    rounds
        .iter()
        .map(|round| score(round))
        .fold(0, |acc, curr| acc + curr)
}

fn part2(rounds: &[&str]) -> i32 {
    fn score(round: &str) -> i32 {
        match round {
            "A X" => 0 + 3,
            "A Y" => 3 + 1,
            "A Z" => 6 + 2,
            "B X" => 0 + 1,
            "B Y" => 3 + 2,
            "B Z" => 6 + 3,
            "C X" => 0 + 2,
            "C Y" => 3 + 3,
            "C Z" => 6 + 1,
            _ => panic!("Impossible round {}", round),
        }
    }
    rounds
        .iter()
        .map(|round| score(round))
        .fold(0, |acc, curr| acc + curr)
}

fn main() {
    let input = include_str!("../../../src/02/input.txt");
    let input = process_input(input);
    println!("Part one: {}", part1(&input));
    println!("Part two: {}", part2(&input));
}
