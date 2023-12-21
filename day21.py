with open("day21.txt", "r") as f:
    lines = f.read().splitlines()

s_coord = (0,0)
for idy, line in enumerate(lines):
    if "S" in line:
        s_coord = (line.find("S"), idy)
    
lines = [[*line] for line in lines]
min_x, min_y = 0, 0

max_x = len(lines[0])
max_y = len(lines)

neigh = [(-1,0), (0,-1), (1,0), (0,1)]

from collections import deque

def part1():
    queue = deque()
    queue.append((0, s_coord))
    steps = 64
    while queue:
        step, point = queue.popleft()
        if step >= steps:
            break
        else:
            # in bounds
            for n in neigh:
                new_x = point[0]+n[0]
                new_y = point[1]+n[1]
                if min_x<=new_x<=max_x and min_y<=new_y<=max_y:
                    if lines[new_y][new_x]!='#' and (step+1, (new_x, new_y)) not in queue:
                        queue.append((step+1, (new_x, new_y)))
    print(len(queue)+1)
    
def pretty_print(obj, queue):
    for idy, line in enumerate(obj):
        new_line = ""
        for idx, c in enumerate(line):
            if (idx,idy) in queue:
                chr = 'O'
            else:
                chr = c
            new_line += chr
        print(new_line)

from datetime import datetime
from multiprocessing import Pool


def part2(steps):
    s = datetime.now()
    queue = deque()
    queue.append((0, s_coord))
    step = 0
    visited = set()
    while queue:
        step, point = queue.popleft()
        if step == steps:
            break
        else:
            # in bounds
            for n in neigh:
                new_x = point[0]+n[0]
                new_y = point[1]+n[1]
                if lines[new_y%max_y][new_x%max_x]!='#' and (step+1, (new_x, new_y)) not in visited:
                    queue.append((step+1, (new_x, new_y)))
                    visited.add((step+1, (new_x, new_y)))
            # in bounds
            
    return(len(queue)+1)
    
from functools import cache

@cache
def get_neighbours(point):
    x, y = point
    valids = deque()
    for n in neigh:
        new_x = x+n[0]
        new_y = y+n[1]
        if lines[new_y%max_y][new_x%max_x]!='#':
            valids.append((new_x, new_y))
    valids = deque(set(valids))
        
    return valids

if __name__ == '__main__':
    steps = 26501365
    leftover = steps%len(lines)
    full = steps//len(lines)
    square_len = len(lines)
    a0 = part2(leftover)
    print(a0)
    a1 = part2(leftover + square_len)
    print(a1)
    a2 = part2(leftover + 2 * square_len)
    print(a2)

    b0 = a0
    b1 = a1-a0
    b2 = a2-a1
    print(b0 + b1*full + (full*(full-1)//2)*(b2-b1))
