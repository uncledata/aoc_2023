from functools import cache

with open("day15.txt", "r") as f:
    lines = f.read().splitlines()

line = lines[0]


@cache
def sequence(curr, ch):
    num = ord(ch)
    curr += num
    curr *= 17
    curr = curr % 256
    return curr


def part1():
    sm = 0

    for sq in line.split(","):
        curr = 0
        for ch in sq:
            curr = sequence(curr, ch)
        sm += curr
    print(sm)


# part1()
def get_sq_score(sq):
    curr = 0
    for ch in sq:
        curr = sequence(curr, ch)
    return curr


boxes = {}

for seq in line.split(","):
    if "=" in seq:
        sq, focal_len = seq.split("=")
        box_num = get_sq_score(sq)
        contents = boxes.get(box_num, []).copy()
        new_box_cont = []
        rpl = False
        if contents == []:
            new_box_cont = [(sq, focal_len)]
        else:
            for i in contents:
                if sq == i[0]:
                    new_box_cont.append((sq, focal_len))
                    rpl = True
                else:
                    new_box_cont.append(i)
            if not rpl:
                new_box_cont.append((sq, focal_len))
        boxes[box_num] = new_box_cont.copy()
        # handle key exists/ not
    elif "-" in seq:
        sq, focal_len = seq.split("-")
        box_num = get_sq_score(sq)
        contents = boxes.get(box_num, []).copy()
        new_box_cont = []
        for i in contents:
            if not (sq == i[0]):
                new_box_cont.append(i)
            else:
                sq = ""

        boxes[box_num] = new_box_cont.copy()

total_focal_power = 0

for i in range(256):
    cont = boxes.get(i, []).copy()
    for idx, vals in enumerate(cont):
        k, fl = vals
        total_focal_power += int(fl) * (idx + 1) * (i + 1)
print(total_focal_power)
