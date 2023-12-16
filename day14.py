with open("day14.txt", "r") as f:
    lines = f.read().splitlines()
cycles = 1_000_000_000


def tilt_around(cur_layout):
    matrix = []
    for line in cur_layout:
        nl = []
        ln = "".join(line)
        for segm in ln.split("#"):
            dots = segm.count(".")
            rounds = "".join(segm.split(".")) + "".join(["."] * dots)
            nl.append(rounds)
        tilted = "#".join(nl)
        matrix.append(tilted)
    return matrix


def pretty_print(obj_list):
    for obj in obj_list:
        print(obj)


seen = {}
loop = -1


def calc_weight(m):
    weigh = 0
    for line in m:
        line_weigh = 0
        for idx, char in enumerate(line):
            if char == "O":
                line_weigh += len(line) - idx
        weigh += line_weigh
    return weigh


loop_start = -1
curr = [[*line] for line in lines]
for i in range(1, 500):
    curr = list(zip(*curr))
    curr = tilt_around(curr)
    curr = list(zip(*curr))
    # west

    curr = tilt_around(curr)
    # south

    curr = list(reversed(curr))
    curr = list(zip(*curr))
    curr = tilt_around(curr)
    curr = list(zip(*curr))
    curr = list(reversed(curr))

    # east
    curr = [list(reversed(line)) for line in curr]
    curr = tilt_around(curr)
    curr = [list(reversed(line)) for line in curr]

    full_string = "|".join(["".join(line) for line in curr])
    w = calc_weight(list(zip(*curr)))
    if seen.get(full_string, 0) == 0:
        seen[full_string] = {i: w}
    else:
        print(i, "seen at:", seen[full_string])
        loop_start = list(seen[full_string].keys())[0]
        print("loop = ", i - max(seen[full_string].keys()))
        loop = i - max(seen[full_string].keys())
        seen[full_string] = seen[full_string] | {i: w}
        break

dct = {}
for d in seen.values():
    dct = dct | d

print(dct[(cycles - loop_start) % loop + loop_start])
