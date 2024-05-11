graph = {
    "A": ["C", "B"],
    "B": ["A", "D"],
    "C": ["A", "G", "H", "I"],
    "D": ["B", "E", "F"],
    "E": ["D"],
    "F": ["D"],
    "G": ["C"],
    "H": ["C"],
    "I": ["C", "J"],
    "J": ["I"],
}

need_visit = ["A"]
visited = []

step = 1
while len(need_visit) > 0:
    node = need_visit.pop()

    if node not in visited:
        visited.append(node)
        need_visit += graph[node]

    print(f"#{step}")
    print(f"node: {node}")
    print(f"visited: {visited}")
    print(f"need_visit: {need_visit}")
    step += 1

print(visited)
