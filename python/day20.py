from collections import deque
import math

with open("day20.txt", "r") as f:
    lines = f.read().splitlines()


class FlipFlop:
    def __init__(self, name):
        self.name = name
        self.is_on = False

    def signal(self, value, name):
        if value == -1:
            if not self.is_on:
                send_val = 1
            else:
                send_val = -1
            self.is_on = not self.is_on
            return send_val
        else:
            return 0

    def __repr__(self):
        return self.__class__.__name__ + ": " + self.name


class Conjunction:
    def __init__(self, name):
        self.nodes = {}
        self.name = name

    def signal(self, value, name):
        if self.nodes:
            self.nodes = self.nodes | {name: value}
        else:
            self.nodes = {name: value}
        if all([val == 1 for _, val in self.nodes.items()]):
            return -1
        else:
            return 1

    def add_connected_nodes(self, nodes_list):
        for node in nodes_list:
            self.nodes[node] = -1

    def __repr__(self):
        return self.__class__.__name__ + ": " + self.name


class Broadcaster:
    def __init__(self, name):
        self.name = name

    def signal(self, value, name):
        return value

    def __repr__(self):
        return self.__class__.__name__ + ": " + self.name


def parse_input(lines):
    nodes = {}
    for line in lines:
        from_node, to_nodes = line.split("->")
        from_node = from_node.strip()
        to_nodes = [node.strip() for node in to_nodes.strip().split(",")]
        node_class = Broadcaster("broadcaster")
        if "%" in from_node:
            node_class = FlipFlop(from_node.replace("%", ""))
        elif "&" in from_node:
            node_class = Conjunction(from_node.replace("&", ""))

        nodes[from_node.replace("%", "").replace("&", "")] = (node_class, to_nodes)
    return nodes


nodes = parse_input(lines)

connected_nodes = {}
conjunction_nodes = []
flip_flops = []
for node_name, node_info in nodes.items():
    if node_info[0].__class__.__name__ == "Conjunction":
        connected_nodes[node_name] = []
        conjunction_nodes.append(node_name)
    if node_info[0].__class__.__name__ == "FlipFlop":
        flip_flops.append(node_name)
for con_node in conjunction_nodes:
    for node_name, node_info in nodes.items():
        if con_node in node_info[1]:
            connected_nodes[con_node] = connected_nodes[con_node] + [node_name]
for conj_node, con_node_list in connected_nodes.items():
    node_class, node_links = nodes[conj_node]
    node_class.add_connected_nodes(con_node_list)
    nodes[conj_node] = (node_class, node_links)


def part1():
    low = 0
    high = 0
    button_clicks = 1000

    for _ in range(1, button_clicks + 1):
        q = deque()
        q.append(("button", "broadcaster", -1))
        while q:
            from_node, node_name, current = q.popleft()
            if current == -1:
                low += 1
            elif current == 1:
                high += 1
            if current != 0:
                print(
                    from_node,
                    " - ",
                    "low" if current == -1 else "high",
                    " -> ",
                    node_name,
                )
                if nodes.get(node_name):
                    current = nodes[node_name][0].signal(current, from_node)
                    for n in nodes[node_name][1]:
                        q.append((node_name, n, current))
    print(low * high)


relevant = {"vt": 0, "sk": 0, "xc": 0, "kk": 0}
cond = True
button_clicks = 0
while cond:
    button_clicks += 1
    q = deque()
    q.append(("button", "broadcaster", -1))
    while q:
        from_node, node_name, current = q.popleft()
        if current != 0:
            # print(from_node," - ", 'low' if current ==-1 else 'high', " -> ", node_name )
            # relevant node changed
            if relevant.get(node_name, -1) >= 0 and current == -1:
                if relevant[node_name] == 0:
                    relevant[node_name] = button_clicks
            if all([val != 0 for _, val in relevant.items()]):
                print(math.lcm(*[val for _, val in relevant.items()]))
                cond = False
            if nodes.get(node_name):
                current = nodes[node_name][0].signal(current, from_node)
                for n in nodes[node_name][1]:
                    q.append((node_name, n, current))
