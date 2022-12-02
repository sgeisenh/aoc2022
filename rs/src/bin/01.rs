fn process_input(input: &str) -> Vec<i32> {
    let mut elves: Vec<i32> = input
        .split("\n\n")
        .map(str::trim)
        .map(|section| {
            section
                .split("\n")
                .map(|line| {
                    line.trim()
                        .parse::<i32>()
                        .expect("Unable to parse line as an integer")
                })
                .sum()
        })
        .collect();
    elves.sort();
    elves.reverse();
    elves
}

fn part1(elves: &[i32]) -> i32 {
    elves[0]
}

fn part2(elves: &[i32]) -> i32 {
    elves.iter().take(3).sum()
}

fn main() {
    let input = include_str!("../../../src/01/input.txt");
    let mut processed = process_input(input);
    println!("Part 1: {}", part1(&processed));
    println!("Part 2: {}", part2(&mut processed));
}
