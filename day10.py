from helpers import read_file_str, INPUTS_PATH, DEMO_PATH
import sys

sys.setrecursionlimit(100000)

DAY = 10
IS_PROD = True

file_name = DEMO_PATH.format(str(DAY)) if not IS_PROD else INPUTS_PATH.format(str(DAY))

lines = read_file_str(file_name)
lines = [line.replace("\n", "") for line in lines]

animal = (0, 0)
for idy, line in enumerate(lines):
    for idx, char in enumerate(line):
        if char == "S":
            animal = (idx, idy)
            break


def pretty_map_print(lines):
    for line in lines:
        print(line)


neighbours = {(1, 0): "R", (0, 1): "D", (0, -1): "U", (-1, 0): "L"}
bounds_y = len(lines)
bounds_x = len(lines[0])
map_ints = []
for idy in range(0, bounds_y):
    cur_line = []
    for idx in range(0, bounds_x):
        cur_line.append(0)
    map_ints.append(cur_line)

map_ints[animal[1]][animal[0]] = 1


def update_map(map_ints, new_coord, curr_cntr):
    map_n = map_ints.copy()
    if map_n[new_coord[1]][new_coord[0]] == -1:
        # print("back_to_start")
        return False
    elif map_n[new_coord[1]][new_coord[0]] == 0:
        map_n[new_coord[1]][new_coord[0]] = curr_cntr + 1
        # pretty_map_print(map_n)
        return True
    elif map_n[new_coord[1]][new_coord[0]] < curr_cntr + 1:
        map_n[new_coord[1]][new_coord[0]] = min(
            curr_cntr, map_n[new_coord[1]][new_coord[0]]
        )
        # print("been there before, but now we have a shorter path")
        # pretty_map_print(map_n)
        # been there before, but now we have a shorter path
        return False
    else:
        map_n[new_coord[1]][new_coord[0]] = curr_cntr + 1
        # print("first_time")
        # pretty_map_print(map_n)
        return True


def potential_dirs(curr):
    vals = {
        (curr[0] + neigh[0], curr[1] + neigh[1]): val
        for neigh, val in neighbours.items()
        if (curr[0] + neigh[0] >= 0 and curr[0] + neigh[0] < bounds_x)
        and curr[1] + neigh[1] >= 0
        and curr[1] + neigh[1] < bounds_y
    }
    return vals


"""
7 right/up -> (1,1)/(-1,-1)
L left/down -> (-1,-1)/(1,1)
J right/down -> (1,-1)/(-1,1)
F up/left -> (1,-1)/(-1,1)
- left/right -> (-1,0)/(1,0)
| up/down -> (0,1)/(0,-1)
"""


def navigate(lines, curr):
    dirs = potential_dirs(curr)
    curr_cntr = map_ints[curr[1]][curr[0]]
    for dir_coord, dir in dirs.items():
        cur_check_obj = lines[dir_coord[1]][dir_coord[0]]
        if cur_check_obj != ".":
            if dir == "R" and cur_check_obj in ("7", "-", "J"):
                if update_map(map_ints, dir_coord, curr_cntr):
                    curr = dir_coord
                    navigate(lines, curr)
            elif dir == "U" and cur_check_obj in ("7", "F", "|"):
                if update_map(map_ints, dir_coord, curr_cntr):
                    curr = dir_coord
                    navigate(lines, curr)
            elif dir == "L" and cur_check_obj in ("F", "-", "L"):
                if update_map(map_ints, dir_coord, curr_cntr):
                    curr = dir_coord
                    navigate(lines, curr)
            elif dir == "D" and cur_check_obj in ("L", "J", "|"):
                if update_map(map_ints, dir_coord, curr_cntr):
                    curr = dir_coord
                    navigate(lines, curr)


navigate(lines, animal)

m = 0
for i in range(0, bounds_y):
    tmp = max(m, max(map_ints[i]))
    m = tmp


print(m - 1)
pretty_map_print(map_ints)
