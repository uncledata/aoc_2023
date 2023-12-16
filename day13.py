with open("day13.txt", "r") as f:
    lines = f.read().splitlines()
lines.append("")


def get_pattern_info(lst):
    for i in range(1, len(lst)):
        arr1 = list(reversed(lst[:i]))
        arr2 = list(lst[i : i + len(arr1)])
        arr1 = arr1[: len(arr2)]
        if arr1 == arr2:
            return i
    return 0


def get_pattern_transposed(lst):
    return list(
        reversed(["".join(reversed(line)) for line in list(reversed(list(zip(*lst))))])
    )


def part1():
    pattern = []
    sm = 0
    horizontal = 0
    vertical = 0
    for idx, line in enumerate(lines):
        if line == "" or idx == len(lines) - 1:
            vertical = get_pattern_info(pattern)
            if vertical == 0:
                pat = get_pattern_transposed(pattern)
                horizontal = get_pattern_info(pat)
                sm += horizontal
            else:
                sm += vertical * 100
            pattern = []
        else:
            pattern.append(line)

    print(sm)


def comp_lists(lst1, lst2):
    if lst1 == lst2:
        return -1
    for i in range(len(lst1)):
        new_list1 = lst1[:i] + lst1[i + 1 :]
        new_list2 = lst2[:i] + lst2[i + 1 :]
        if new_list1 == new_list2:
            return i
    return -1


def comp_strings(str1, str2):
    if str1 == str2:
        return -1
    for i in range(len(str1)):
        new_str1 = str1[:i] + str1[i + 1 :]
        new_str2 = str2[:i] + str2[i + 1 :]
        if new_str1 == new_str2:
            return i
    return -1


def get_pattern_info_p2(lst):
    for i in range(1, len(lst)):
        arr1 = list(reversed(lst[:i]))
        arr2 = list(lst[i : i + len(arr1)])
        arr1 = arr1[: len(arr2)]
        idx = comp_lists(arr1, arr2)
        if idx != -1:
            if comp_strings(arr1[idx], arr2[idx]) != -1:
                return i
    return 0


def part2():
    pattern = []
    sm = 0
    for idx, line in enumerate(lines):
        if line == "" or idx == len(lines) - 1:
            # vertical = get_pattern_info(pattern)
            vertical_2 = get_pattern_info_p2(pattern)
            pat = get_pattern_transposed(pattern)
            horizontal_2 = get_pattern_info_p2(pat)
            if vertical_2 != 0:
                sm += vertical_2 * 100
            elif horizontal_2 != 0:
                sm += horizontal_2
            pattern = []
        else:
            pattern.append(line)
    print(sm)


part1()
part2()
