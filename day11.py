with open("day11.txt", 'r') as f:
    lines = f.readlines()
lines_new = []
for line in lines:
    lines_new.append([*(line.replace("\n",""))])

coords = []
for idy in range(len(lines_new)):
    for idx in range(len(lines_new[0])):
        if lines_new[idy][idx]=='#':
            coords.append((idx,idy))

coord_x = set([coord[0] for coord in coords])
coord_y = set([coord[1] for coord in coords])

missing_x = set(list(range(0,len(lines_new))))-coord_x
missing_y = set(list(range(0,len(lines_new[1]))))-coord_y


multiplier = 1000000-1 # part1 -> 2 - 1

new_coords = []
for coord in coords:
    x_adjust = len([miss_x for miss_x in missing_x if coord[0]>miss_x])* multiplier
    y_adjust = len([miss_y for miss_y in missing_y if coord[1]>miss_y])* multiplier
    new_coords.append((coord[0]+x_adjust, coord[1]+y_adjust))

def steps(coorda, coordb):
    return abs(coorda[0]-coordb[0])+abs(coorda[1]-coordb[1])
print("calc paths")
paths = 0
for i in range(len(new_coords)-1):
    for j in range(i, len(new_coords)):
        paths +=steps(new_coords[i], new_coords[j])

print(paths)
