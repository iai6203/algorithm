import heapq

N, M = map(int, input().split())
start = "1"

graph = {}
for i in range(0, M):
    A, B, weight = input().split()

    if not graph.get(A):
        graph[A] = {}
    if not graph.get(B):
        graph[B] = {}

    graph[A][B] = int(weight)
    graph[B][A] = int(weight)


def solution():
    distances = {}
    for key in graph:
        distances[key] = float("inf")
    distances[start] = 0

    queue = []
    heapq.heappush(queue, [0, start])

    while len(queue) > 0:
        current_item_distance, current_item_key = heapq.heappop(queue)

        if current_item_distance > distances[current_item_key]:
            continue

        for adjacent_key, adjacent_distance in graph[current_item_key].items():
            distance = current_item_distance + adjacent_distance

            if distance < distances[adjacent_key]:
                distances[adjacent_key] = distance
                heapq.heappush(queue, [distance, adjacent_key])

    print(distances)


solution()
