import heapq


with open("inputs/day17.txt") as f:
    data = [list(map(int, [*line])) for line in f.read().splitlines()]

directions = set([(0, -1), (0, 1), (-1, 0), (1, 0)])


def heapq_min_heat(start, end, least, most):
    queue = [(0, start[0], start[1], 0, 0)]
    visited = set()

    while queue:
        heat, x, y, px, py = heapq.heappop(queue)

        if (x, y) == end:
            return heat

        if (x, y, px, py) in visited:
            continue

        visited.add((x, y, px, py))

        for dx, dy in directions - set([(px, py)]) - set([(-px, -py)]):
            nx, ny, h = x, y, heat

            for i in range(1, most + 1):
                nx, ny = nx + dx, ny + dy

                # check if in bounds
                if 0 <= nx < len(data[0]) and 0 <= ny < len(data):
                    h += data[ny][nx]

                    if i >= least:
                        heapq.heappush(queue, (h, nx, ny, dx, dy))


start = (0, 0)
end = (len(data[0]) - 1, len(data) - 1)

print(heapq_min_heat(start, end, 1, 3))
print(heapq_min_heat(start, end, 4, 10))
