
use std::fs::read_to_string;
use std::time::Instant;

fn main() {
    let start_time = Instant::now();
    let mut sum = 0;
    let mut sum2 = 0;
    for line in read_to_string("./inputs/input.txt").expect("failed to read file").lines() {
        sum += get_first_last_digits(line.to_owned());
        sum2 += get_first_last_digits(adjust_line_get_digits(line));
    }
    println!("Part1: {}", sum);
    println!("Part2: {}", sum2);

    let elapsed_time = start_time.elapsed();

    println!("Elapsed time: {:?}", elapsed_time);

}

fn adjust_line_get_digits(inp: &str) -> String {
    let new_inp = inp.replace("one", "o1e")
    .replace("two", "t2o")
    .replace("three", "t3e")
    .replace("four", "f4r")
    .replace("five", "f5e")
    .replace("six", "s6x")
    .replace("seven", "s7n")
    .replace("eight", "e8t")
    .replace("nine", "n9e")
    .replace("zero", "z0o");
    return new_inp;

}

fn get_first_last_digits(inp: String) -> i32{
    let inp = inp.chars();
    let mut first_dig = -1;
    let mut last_dig = -1;
    for i in inp {
        if i.is_digit(10) {
            if first_dig == -1 {
                first_dig = i.to_digit(10).expect("not an int of base 10") as i32;
            }
            last_dig = i.to_digit(10).expect("not an int of base 10")  as i32;
        }
    }
    let res = (first_dig * 10) + last_dig;
    return res
}