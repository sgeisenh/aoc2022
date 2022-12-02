#![feature(binary_heap_into_iter_sorted)]

use std::collections::BinaryHeap;

fn process_input(input: &str) -> BinaryHeap<i32> {
    input
        .split("\n\n")
        .map(str::trim)
        .map(|section| {
            section
                .split('\n')
                .map(|line| {
                    line.trim()
                        .parse::<i32>()
                        .expect("Unable to parse line as an integer")
                })
                .sum()
        })
        .collect()
}

fn part1(elves: &BinaryHeap<i32>) -> i32 {
    *elves.peek().expect("Should be at least one elf")
}

fn part2(elves: BinaryHeap<i32>) -> i32 {
    elves.into_iter_sorted().take(3).sum()
}

fn main() {
    let input = include_str!("../../../src/01/input.txt");
    let input = process_input(input);
    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(input));
}
