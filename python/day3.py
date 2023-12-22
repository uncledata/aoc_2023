from helpers import read_file_str, INPUTS_PATH, DEMO_PATH, download_input

IS_PROD = True
DAY = 3

not_count = ["."]


def check_surround(num, row_idx, col_idx, lines):
    start_x = max(0, col_idx - len(num))
    end_x = min(len(lines[0]), col_idx + 2)
    start_y = max(0, row_idx - 1)
    end_y = min(len(lines) - 1, row_idx + 1)
    vals_surround = ""
    vals_surround = vals_surround + lines[start_y][start_x:end_x]
    vals_surround = vals_surround + lines[end_y][start_x:end_x]
    if start_y != row_idx:
        vals_surround = vals_surround + lines[row_idx][start_x:end_x]
    vals_surround = vals_surround.replace("\n", "").replace(num, "")
    for char in not_count:
        vals_surround = vals_surround.replace(char, "")

    if "*" in vals_surround:
        star_coords = []
        for y, line in enumerate(lines[start_y : end_y + 1]):
            for x, char in enumerate(line[start_x:end_x]):
                if char == "*":
                    star_coords.append((start_x + x, start_y + y))
        return len(vals_surround), True, star_coords
    else:
        return len(vals_surround), False, []


def part1(lines):
    sum = 0
    sum_2 = 0
    star_seen_counter = {}
    for row_idx, line in enumerate(lines):
        cur_num = ""
        for col_idx, char in enumerate(line):
            if char.isdigit():
                # construct number
                cur_num += char
            if (
                col_idx < len(line) - 1
                and (not line[col_idx + 1].isdigit())
                and cur_num != ""
                and line[col_idx].isdigit()
            ):
                num, has_star, star_coords = check_surround(
                    cur_num, row_idx, col_idx, lines
                )
                if num != 0:
                    sum += int(cur_num)
                    if has_star:
                        for star_coord in star_coords:
                            cur_list = star_seen_counter.get(star_coord, [])
                            cur_list.append(cur_num)
                            star_seen_counter[star_coord] = cur_list
            if not char.isdigit():
                cur_num = ""
    print(sum)
    for key, val in star_seen_counter.items():
        if len(val) == 2:
            sum_2 += int(val[0]) * int(val[1])
    print(sum_2)


if __name__ == "__main__":
    if IS_PROD:
        download_input(str(DAY))
        file_path = INPUTS_PATH.format(str(DAY))
    else:
        file_path = DEMO_PATH.format(str(DAY))
    sum = 0
    lines = read_file_str(file_path)
    part1(lines)
