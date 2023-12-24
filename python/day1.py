from helpers import read_file_str
from datetime import datetime

DAY = 1


def get_first_last_digits(inp: str) -> int:
    first_dig: int = 10
    last_dig: int = 10
    for ch in inp:
        if ch.isdigit():
            if first_dig == 10:
                first_dig = int(ch)
            last_dig = int(ch)
    return first_dig * 10 + last_dig


def adjust_line_get_digits(inp: str) -> str:
    return (
        inp.replace("one", "o1e")
        .replace("two", "t2o")
        .replace("three", "t3e")
        .replace("four", "f4r")
        .replace("five", "f5e")
        .replace("six", "s6x")
        .replace("seven", "s7n")
        .replace("eight", "e8t")
        .replace("nine", "n9e")
        .replace("zero", "z0o")
    )


if __name__ == "__main__":
    start = datetime.now()
    lines = read_file_str("input.txt")
    sm1 = 0
    sm2 = 0
    with open("input.txt") as f:
        for line in f.read().splitlines():
            sm1 += get_first_last_digits(line)
            sm2 += get_first_last_digits(adjust_line_get_digits(line))
    print("Part 1: ", sm1)
    print("Part 2: ", sm2)
    print("Elapsed time: ", int(str(datetime.now() - start)[-6:]) / 1000.0, "ms")
