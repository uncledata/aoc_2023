from helpers import read_file_str, INPUTS_PATH, DEMO_PATH, download_input

IS_PROD = True
DAY = 2

LIMITS = {"red": 12, "green": 13, "blue": 14}


def parse_round_input(str_input):
    parsed_game = []
    input = str_input.split(":")[1].strip().split(";")
    input = [val.split(",") for val in input]
    for i in range(0, len(input)):
        round_val = []
        for j in range(0, len(input[i])):
            game_input = input[i][j].strip().split(" ")
            tmp_val = (game_input[1], game_input[0])
            round_val.append(tmp_val)
        parsed_game.append(round_val)
    return parsed_game


def validate_p1(round_val):
    possible_round = 1
    for _, round_to_validate in enumerate(round_val):
        for _, detail_to_validate in enumerate(round_to_validate):
            if LIMITS[detail_to_validate[0]] < int(detail_to_validate[1]):
                possible_round = 0
    return possible_round


def part2(game_val):
    min_cubes = {}
    for _, round in enumerate(game_val):
        for _, cube in enumerate(round):
            print(min_cubes.get(cube[0], 0), int(cube[1]))
            if min_cubes.get(cube[0], 0) < int(cube[1]):
                min_cubes[cube[0]] = int(cube[1])
    result = 1
    for val in min_cubes.values():
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
        parsed = parse_round_input(line)
        valid_game = validate_p1(parsed)
        if valid_game:
            idx_sum += idx + 1
        part2_sum += part2(parsed)

    print(idx_sum)
    print(part2_sum)
