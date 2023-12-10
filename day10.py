from helpers import read_file_str, INPUTS_PATH, DEMO_PATH
import sys

sys.setrecursionlimit(100000)

DAY = 10
IS_PROD = False

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


with open("day_10_outp.txt", "w+") as f:
    for line in map_ints:
        f.write(" ".join([str(chr) for chr in line]) + "\n")


with open("/Users/tomaspeluritis/aoc_2023/day_10_outp.txt", "r") as f:
    lines = f.readlines()
lines = [line.replace("\n", "").split(" ") for line in lines]

fixed_lines = []
for line in lines:
    cur_line = []
    for char in line:
        cur_line.append(9 if char != "0" else 0)
    fixed_lines.append(cur_line)
bounds_y = len(fixed_lines)
bounds_x = len(fixed_lines[0])

for idy in range(0, bounds_y):
    if fixed_lines[idy][0] == 0:
        fixed_lines[idy][0] = "#"
    if fixed_lines[idy][bounds_x - 1] == 0:
        fixed_lines[idy][bounds_x - 1] = "#"

for idx in range(0, bounds_x):
    if fixed_lines[0][idx] == 0:
        fixed_lines[0][idx] = "#"
    if fixed_lines[bounds_y - 1][idx] == 0:
        fixed_lines[bounds_y - 1][idx] = "#"

neighbours_coords_only = list(neighbours.keys())
cur_map = fixed_lines.copy()
cond = True
while cond:
    cnt = 0
    for idy in range(1, bounds_y - 1):
        for idx in range(1, bounds_x - 1):
            if cur_map[idy][idx] not in ("#", 9) and any(
                [
                    cur_map[idy + neigh[1]][idx + neigh[0]] == "#"
                    for neigh in neighbours_coords_only
                ]
            ):
                cur_map[idy][idx] = "#"
                cnt += 1
    if cnt == 0:
        cond = False


ttl_cnt = 0
for idy in range(0, bounds_y):
    for idx in range(0, bounds_x):
        ttl_cnt += 1 if cur_map[idy][idx] == 0 else 0
print(ttl_cnt)
