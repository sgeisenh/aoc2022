fn process_input(input: &str) -> Vec<&str> {
    input.lines().map(str::trim).collect()
}

fn item_to_priority(item: char) -> i32 {
    let item = item as u8;
    match item {
        b'a'..=b'z' => (item - b'a' + 1).into(),
        b'A'..=b'Z' => (item - b'A' + 27).into(),
        _ => panic!("Invalid item: {}", item),
    }
}

fn part1(lines: &[&str]) -> i32 {
    lines
        .iter()
        .map(|line| {
            let (first, second) = line.split_at(line.len() / 2);
            first
                .chars()
                .filter(|c| second.contains(*c))
                .map(item_to_priority)
                .next()
                .expect("Invalid line does not contain misplaced item")
        })
        .sum()
}

fn part2(lines: &[&str]) -> i32 {
    lines
        .chunks(3)
        .map(|chunk| {
            let mut candidates = chunk[0].chars().collect::<Vec<_>>();
            for line in &chunk[1..] {
                candidates = line.chars().filter(|c| candidates.contains(c)).collect();
            }
            item_to_priority(candidates[0])
        })
        .sum()
}

fn main() {
    let input = include_str!("../../../src/03/input.txt");
    let input = process_input(input);
    println!("Part one: {}", part1(&input));
    println!("Part two: {}", part2(&input));
}
