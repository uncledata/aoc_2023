from math import prod

import networkx as nx

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    G = nx.Graph()

    for line in lines:
        k, vals = line.split(":")
        k = k.strip()
        vals = vals.strip().split(" ")
        for val in vals:
            G.add_edge(val, k)

    G.remove_edges_from(nx.minimum_edge_cut(G))

    print(prod([len(c) for c in nx.connected_components(G)]))
