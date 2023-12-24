from z3 import Int, Ints, Solver

with open("input.txt") as f:
    lines = f.read().splitlines()


def parse_string(s):
    s = s.split("@")
    p = [int(x.strip()) for x in s[0].strip().split(",")]
    speed = [int(x.strip()) for x in s[1].strip().split(",")]

    return p, speed


x = (200000000000000, 400000000000000)
y = (200000000000000, 400000000000000)
# x = (7, 27)
# y = (7, 27)


def get_slope(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    m = (y2 - y1) / (x2 - x1)
    c = y1 - m * x1
    return (m, c)


def is_intersecting(p1, slope1, inter1, x_speed1, p2, slope2, inter2, x_speed2):
    global x, y
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    # Check if lines are parallel
    if slope1 == slope2:
        return False

    # Calculate intersection point
    x_i, y_i = (
        (inter2 - inter1) / (slope1 - slope2),
        slope1 * (inter2 - inter1) / (slope1 - slope2) + inter1,
    )
    t1 = (x_i - x1) / x_speed1
    t2 = (x_i - x2) / x_speed2
    # z_intersect = z1 + c1 * t
    if t1 < 0 or t2 < 0:
        return False
    if x_i >= x[0] and x_i <= x[1] and y_i >= y[0] and y_i <= y[1]:
        return True
    else:
        return False


cnt = 0
for idx, line in enumerate(lines):
    p1, s1 = parse_string(line)
    p1_2 = [p1[0] + s1[0], p1[1] + s1[1], p1[2] + s1[2]]
    m1, c1 = get_slope(p1, p1_2)
    for idy in range(idx + 1, len(lines)):
        line2 = lines[idy]
        if idx == idy:
            continue
        p2, s2 = parse_string(line2)
        p2_2 = [p2[0] + s2[0], p2[1] + s2[1], p2[2] + s2[2]]
        m2, c2 = get_slope(p2, p2_2)
        cnt += is_intersecting(p1, m1, c1, s1[0], p2, m2, c2, s2[0])
print(cnt)


lines = [parse_string(line) for line in lines]
lines = [[*line[0], *line[1]] for line in lines]
pxr, pyr, pzr, vxr, vyr, vzr = Ints("pxr pyr pzr vxr vyr vzr")
s = Solver()
for k, h in enumerate(lines):
    tK = Int(f"t{k}")
    s.add(tK > 0)
    pxh, pyh, pzh, vxh, vyh, vzh = h
    s.add(pxr + tK * vxr == pxh + tK * vxh)
    s.add(pyr + tK * vyr == pyh + tK * vyh)
    s.add(pzr + tK * vzr == pzh + tK * vzh)
s.check()
pxr = s.model()[pxr].as_long()
pyr = s.model()[pyr].as_long()
pzr = s.model()[pzr].as_long()
print(pxr + pyr + pzr)
