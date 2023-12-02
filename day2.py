from helpers import read_file_str, INPUTS_PATH, DEMO_PATH, download_input
import re

IS_PROD = True
DAY = 2

LIMITS = {"red": 12, "green": 13, "blue": 14}


def prep(input):
    inp = [val.strip() for val in re.split(r":|,|;", input)]
    inp.pop(0)
    return inp


def part1(input):
    for round in input:
        num, color = round.split(" ")
        if int(num) > LIMITS[color]:
            return 0
    return 1


def part2(game_val):
    min_vals = {}
    for fig in game_val:
        num, color = fig.split(" ")
        if min_vals.get(color, 0) < int(num):
            min_vals[color] = int(num)
    result = 1
    for val in min_vals.values():
        result = result * val
    return result


if __name__ == "__main__":
    if IS_PROD:
        download_input(str(DAY))
        file_path = INPUTS_PATH.format(str(DAY))
    else:
        file_path = DEMO_PATH.format(str(DAY))
    print(file_path)

    lines = read_file_str(file_path)
    games = []
    idx_sum = 0
    part2_sum = 0
    for idx, line in enumerate(lines):
        parsed = prep(line)
        idx_sum += part1(parsed) * (idx + 1)
        part2_sum += part2(parsed)

    print(idx_sum)
    print(part2_sum)
