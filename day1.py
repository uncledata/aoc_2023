from helpers import read_file_str, download_input, INPUTS_PATH, DEMO_PATH

DAY = 1
IS_PROD = True


def day1_p1(lines):
    tmp = 0
    sum_val = 0
    for line in lines:
        for char in line:
            if char.isdigit():
                tmp = int(char) * 10
                break
        for char in reversed(line):
            if char.isdigit():
                tmp = tmp + int(char)
                break
        sum_val += int(tmp)
    print(sum_val)


def get_nums(str_val):
    nums = ""
    vals = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    cur_idx = 0
    while cur_idx < len(str_val):
        for check in list(vals.keys()):
            if str_val[cur_idx : cur_idx + len(check)].startswith(check):
                nums = nums + str(vals[check])
                # Not skipping last letter of check because it might be a start for another
                cur_idx += len(check) - 2
                break
            elif str_val[cur_idx].isdigit():
                nums = nums + str_val[cur_idx]
                break
        cur_idx += 1
    return nums


def day1_p2(lines):
    tmp = 0
    for line in lines:
        nums = get_nums(line)
        tmp += int(nums[0] + nums[-1])
    print(tmp)


if __name__ == "__main__":
    file_name = (
        DEMO_PATH.format(str(DAY)) if not IS_PROD else INPUTS_PATH.format(str(DAY))
    )
    if IS_PROD:
        download_input(str(DAY))
    lines = read_file_str(file_name)
    day1_p1(lines)
    day1_p2(lines)
