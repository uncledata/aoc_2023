
with open("day8.txt", 'r') as f:
    lines = f.readlines()

from collections import namedtuple
 
# Declaring namedtuple()
Node = namedtuple('Node', ['L', 'R'])

instr = lines[0].replace("\n","")
lines = [line.replace("\n",'').replace(" ","").replace("(","").replace(")","").replace("=",",").split(",") for line in lines[2:]]
nodes = {line[0]:Node(line[1], line[2]) for line in lines}

def part1():
    steps = 0
    cur_node = 'AAA'
    next_node = nodes[cur_node]

    break_loop = False

    while not break_loop:
        for i in instr:
            if cur_node == 'ZZZ':
                break_loop = True
                break
            steps+=1
            cur_node = getattr(next_node,i)
            next_node = nodes[cur_node]
            
    print(steps)
            

ghost_nodes = [key for key, _ in nodes.items() if key[2]=='A']

loop = 0
sm = 0
vals = []
ghost_nodes_cur = ghost_nodes.copy()

steps_till_ends_in_z = {}

cond = True
while cond:
    for i in instr:
        ghost_nodes_cur = [getattr(nodes[node],i) for node in ghost_nodes_cur]
        sm +=1
    for idx, gh in enumerate(ghost_nodes_cur):
        if gh[2]=='Z':
            steps_till_ends_in_z[idx] = sm - steps_till_ends_in_z.get(idx,0)
    if len(steps_till_ends_in_z)==len(ghost_nodes_cur):
        cond = False
print(steps_till_ends_in_z)

from math import lcm
print(lcm(*steps_till_ends_in_z.values()))
