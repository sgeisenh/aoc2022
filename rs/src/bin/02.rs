fn process_input(input: &str) -> Vec<&str> {
    input.lines().map(str::trim).collect()
}

fn part1(rounds: &[&str]) -> i32 {
    fn score(round: &str) -> i32 {
        match round {
            "A X" => 4,
            "A Y" => 8,
            "A Z" => 3,
            "B X" => 1,
            "B Y" => 5,
            "B Z" => 9,
            "C X" => 7,
            "C Y" => 2,
            "C Z" => 6,
            _ => panic!("Impossible round {}", round),
        }
    }
    rounds.iter().map(|round| score(round)).sum()
}

fn part2(rounds: &[&str]) -> i32 {
    fn score(round: &str) -> i32 {
        match round {
            "A X" => 3,
            "A Y" => 4,
            "A Z" => 8,
            "B X" => 1,
            "B Y" => 5,
            "B Z" => 9,
            "C X" => 2,
            "C Y" => 6,
            "C Z" => 7,
            _ => panic!("Impossible round {}", round),
        }
    }
    rounds.iter().map(|round| score(round)).sum()
}

fn main() {
    let input = include_str!("../../../src/02/input.txt");
    let input = process_input(input);
    println!("Part one: {}", part1(&input));
    println!("Part two: {}", part2(&input));
}
