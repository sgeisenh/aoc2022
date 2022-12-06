struct Ranges((i32, i32), (i32, i32));

fn process_input(input: &str) -> Vec<Ranges> {
    input
        .lines()
        .map(str::trim)
        .map(|line| {
            let ranges = line.split(',').collect::<Vec<_>>();
            let left = ranges[0]
                .split('-')
                .map(|section| section.parse().unwrap())
                .collect::<Vec<i32>>();
            let right = ranges[1]
                .split('-')
                .map(|section| section.parse().unwrap())
                .collect::<Vec<i32>>();
            Ranges((left[0], left[1]), (right[0], right[1]))
        })
        .collect()
}

fn part1(ranges: &[Ranges]) -> usize {
    ranges
        .iter()
        .filter(|Ranges((a, b), (c, d))| (a <= c && d <= b) || (c <= a && b <= d))
        .count()
}

fn part2(ranges: &[Ranges]) -> usize {
    ranges
        .iter()
        .filter(|Ranges((a, b), (c, d))| (a <= c && b >= c) || (c <= a && d >= a))
        .count()
}

fn main() {
    let input = include_str!("../../../src/04/input.txt");
    let input = process_input(input);
    println!("Part one: {}", part1(&input));
    println!("Part two: {}", part2(&input));
}
