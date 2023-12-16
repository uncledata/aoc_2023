import sys

sys.setrecursionlimit(10**8)

with open("inputs/day16.txt") as f:
    lines = f.read().splitlines()
lines = [[*line] for line in lines]


path = {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0)}
direction_path_symbol = {"UP": "^", "DOWN": "v", "LEFT": "<", "RIGHT": ">"}
mx_en = 0
visited_matrix = [[0 for _ in range(len(lines[0]))] for _ in range(len(lines))]
visited_matrix_paths = [["." for _ in range(len(lines[0]))] for _ in range(len(lines))]
visited_matrix_dirs = [[[] for _ in range(len(lines[0]))] for _ in range(len(lines))]


def travel(direction, x, y):
    if y == 7 and x == 7:
        print(lines[y][x])
    # exit condition:
    if not (x < 0 or y < 0 or x >= len(lines[0]) or y >= len(lines)):
        if visited_matrix[y][x] >= 1 and direction in visited_matrix_dirs[y][x]:
            return "Loop"
        visited_matrix_dirs[y][x] = visited_matrix_dirs[y][x] + [direction]
        visited_matrix[y][x] = visited_matrix[y][x] + 1
        if lines[y][x] == ".":
            visited_matrix_paths[y][x] = direction_path_symbol[direction]
            travel(direction, x + path[direction][0], y + path[direction][1])
        elif lines[y][x] == "/":
            if direction == "DOWN":
                visited_matrix_paths[y][x] = direction_path_symbol["LEFT"]
                travel("LEFT", x + path["LEFT"][0], y + path["LEFT"][1])
            elif direction == "RIGHT":
                visited_matrix_paths[y][x] = direction_path_symbol["UP"]
                travel("UP", x + path["UP"][0], y + path["UP"][1])
            elif direction == "UP":
                visited_matrix_paths[y][x] = direction_path_symbol["RIGHT"]
                travel("RIGHT", x + path["RIGHT"][0], y + path["RIGHT"][1])
            elif direction == "LEFT":
                visited_matrix_paths[y][x] = direction_path_symbol["DOWN"]
                travel("DOWN", x + path["DOWN"][0], y + path["DOWN"][1])

        elif lines[y][x] == "\\":
            if direction == "UP":
                visited_matrix_paths[y][x] = direction_path_symbol["LEFT"]
                travel("LEFT", x + path["LEFT"][0], y + path["LEFT"][1])
            elif direction == "RIGHT":
                visited_matrix_paths[y][x] = direction_path_symbol["DOWN"]
                travel("DOWN", x + path["DOWN"][0], y + path["DOWN"][1])
            elif direction == "LEFT":
                visited_matrix_paths[y][x] = direction_path_symbol["UP"]
                travel("UP", x + path["UP"][0], y + path["UP"][1])
            elif direction == "DOWN":
                visited_matrix_paths[y][x] = direction_path_symbol["RIGHT"]
                travel("RIGHT", x + path["RIGHT"][0], y + path["RIGHT"][1])

        elif lines[y][x] == "-":
            if direction in ("LEFT", "RIGHT"):
                visited_matrix_paths[y][x] = direction_path_symbol[direction]
                travel(direction, x + path[direction][0], y + path[direction][1])
            elif direction in ("UP", "DOWN"):
                visited_matrix_paths[y][x] = direction_path_symbol["LEFT"]
                travel("LEFT", x + path["LEFT"][0], y + path["LEFT"][1])
                visited_matrix_paths[y][x] = direction_path_symbol["RIGHT"]
                travel("RIGHT", x + path["RIGHT"][0], y + path["RIGHT"][1])
        elif lines[y][x] == "|":
            if direction in ("UP", "DOWN"):
                visited_matrix_paths[y][x] = direction_path_symbol[direction]
                travel(direction, x + path[direction][0], y + path[direction][1])
            elif direction in ("LEFT", "RIGHT"):
                visited_matrix_paths[y][x] = direction_path_symbol["DOWN"]
                travel("DOWN", x + path["DOWN"][0], y + path["DOWN"][1])
                visited_matrix_paths[y][x] = direction_path_symbol["UP"]
                travel("UP", x + path["UP"][0], y + path["UP"][1])

        else:
            return "End"


def re_initiate_matrix():
    global visited_matrix, visited_matrix_paths, visited_matrix_dirs
    visited_matrix = [[0 for _ in range(len(lines[0]))] for _ in range(len(lines))]
    visited_matrix_paths = [
        ["." for _ in range(len(lines[0]))] for _ in range(len(lines))
    ]
    visited_matrix_dirs = [
        [[] for _ in range(len(lines[0]))] for _ in range(len(lines))
    ]


def get_max_energized():
    global mx_en
    cnt = 0
    for i in visited_matrix:
        for j in i:
            if j != 0:
                cnt += 1
    if mx_en < cnt:
        mx_en = cnt


# part1:
re_initiate_matrix()
travel("RIGHT", 0, 0)
get_max_energized()
print(mx_en)

# part2
for i in range(len(lines[0])):
    re_initiate_matrix()
    travel("RIGHT", i, 0)
    get_max_energized()

    re_initiate_matrix()
    travel("DOWN", i, 0)
    get_max_energized()

    re_initiate_matrix()
    travel("LEFT", i, 0)
    get_max_energized()

    re_initiate_matrix()
    travel("RIGHT", i, len(lines) - 1)
    get_max_energized()

    re_initiate_matrix()
    travel("UP", i, len(lines) - 1)
    get_max_energized()

    re_initiate_matrix()
    travel("LEFT", i, len(lines) - 1)
    get_max_energized()


for i in range(1, len(lines) - 1):
    re_initiate_matrix()
    travel("RIGHT", 0, i)
    get_max_energized()

    re_initiate_matrix()
    travel("DOWN", 0, i)
    get_max_energized()

    re_initiate_matrix()
    travel("UP", 0, i)
    get_max_energized()

    re_initiate_matrix()
    travel("DOWN", len(lines[0]) - 1, i)
    get_max_energized()

    re_initiate_matrix()
    travel("UP", len(lines[0]) - 1, i)
    get_max_energized()

    re_initiate_matrix()
    travel("LEFT", len(lines[0]) - 1, i)
    get_max_energized()


print(mx_en)
