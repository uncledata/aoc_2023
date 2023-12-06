with open("day6.txt", "r") as f:
    lines = f.readlines()
time, distance = [line.replace("\n",'').split(":")[1].replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").strip().split(" ") for line in lines]

def get_ways(t, d):
    ways_cnt = 0
    for i in range(1,t):
        speed = i
        left_time = t-i
        if (speed * left_time) > d:
            ways_cnt+=1
    return ways_cnt

lst = []
for idx in range(0,len(time)):
    print(idx)
    print(int(time[idx]), int(distance[idx]))
    lst.append(get_ways(int(time[idx]), int(distance[idx])))

t = int("".join(time))
d = int("".join(distance))
print(get_ways(t,d))
