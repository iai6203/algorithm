import heapq

my_graph = {
    "A": {
        "B": 8,
        "C": 1,
        "D": 2,
    },
    "B": {},
    "C": {
        "B": 5,
        "D": 2,
    },
    "D": {
        "E": 3,
        "F": 5,
    },
    "E": {
        "F": 1,
    },
    "F": {
        "A": 5,
    },
}


def dijkstra(graph, start):
    distances = {}
    for key in graph:
        distances[key] = float("inf")
    distances[start] = 0

    queue = []
    heapq.heappush(queue, [0, start])

    while len(queue) > 0:
        item = heapq.heappop(queue)
        current_item_key = item[1]
        current_item_distance = item[0]

        if current_item_distance > distances[current_item_key]:
            continue

        for adjacent in graph[current_item_key].items():
            adjacent_key = adjacent[0]
            adjacent_distance = adjacent[1]

            distance = current_item_distance + adjacent_distance

            if distances[adjacent_key] > distance:
                distances[adjacent_key] = distance
                heapq.heappush(queue, [distance, adjacent_key])

    return distances


result = dijkstra(my_graph, "A")
print(result)
