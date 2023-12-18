with open("day18.txt", "r") as f:
    lines = [line.split(" ") for line in f.read().splitlines()]
start = (0,0)
path = []
edge = {}
dirs = {"R":(1,0), "L":(-1,0), "U":(0,-1), "D": (0,1)}
map_dirs = {"0":"R","1":"D", "2": "L", "3":"U"}
cur = start

# Shoelace formula
def shoelace(path):
    area = 0
    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        area += x1 * y2 - x2 * y1
    perimeter = len(path)
    inner_area = abs(area) // 2 - perimeter // 2 + 1
    print(inner_area + perimeter)
    

for i in lines:
    for _ in range(int(i[1])):
        cur = (cur[0]+int(dirs[i[0]][0]), cur[1]+int(dirs[i[0]][1]))
        path.append(cur)

#part1
shoelace(path)

#part2
path_p2 = []
cur = start
for i in lines:
    hx = i[2].split("#")[1].replace(")", "")
    ln = int(hx[0:5],16)
    dir = map_dirs[hx[-1]]
    #print(hx, dir, ln)
    for _ in range(ln):
        cur = (cur[0]+int(dirs[dir][0]), cur[1]+int(dirs[dir][1]))
        path_p2.append(cur)

shoelace(path_p2)





                
           
