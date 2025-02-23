from collections import defaultdict

from aocd import data


def parse_connections(network_map):
    connections = {}
    for line in network_map.strip().split("\n"):
        a, b = line.split("-")
        connections.setdefault(a, set()).add(b)
        connections.setdefault(b, set()).add(a)
    return connections


def find_triplets(connections):
    triplets = set()
    computers = list(connections.keys())

    for i in range(len(computers)):
        for j in range(i + 1, len(computers)):
            for k in range(j + 1, len(computers)):
                a, b, c = computers[i], computers[j], computers[k]
                if b in connections[a] and c in connections[a] and c in connections[b]:
                    triplet = tuple(sorted([a, b, c]))
                    triplets.add(triplet)
    return triplets


def count_triplets_with_t(triplets):
    return sum(
        1 for triplet in triplets if any(comp.startswith("t") for comp in triplet)
    )


def find_max_clique(connections):
    nodes = sorted(connections.keys(), key=lambda x: len(connections[x]), reverse=True)
    max_clique = set()

    def is_connected_to_all(node, clique):
        return all(n in connections[node] for n in clique)

    def extend_clique(candidates, clique):
        nonlocal max_clique

        if len(candidates) + len(clique) <= len(max_clique):
            return

        if not candidates:
            if len(clique) > len(max_clique):
                max_clique = clique.copy()
            return

        while candidates:
            v = candidates.pop()
            new_candidates = {u for u in candidates if u in connections[v]}
            if new_candidates or not max_clique or len(clique) + 1 > len(max_clique):
                extend_clique(new_candidates, clique | {v})

    initial_candidates = set(nodes)
    extend_clique(initial_candidates, set())

    return sorted(max_clique)


connections = parse_connections(data)
triplets = find_triplets(connections)
t_count = count_triplets_with_t(triplets)
max_clique = find_max_clique(connections)

print(f"All triplets with 't' computers: {t_count}")

if max_clique:
    password = ",".join(sorted(max_clique))
    print(f"Password: {password}")
