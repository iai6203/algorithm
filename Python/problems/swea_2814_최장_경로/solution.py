import sys

sys.stdin = open("input.txt", "r")


T = int(input())


def search(path):
    global distance

    current = path[len(path) - 1]
    distance = max(distance, len(path))

    for edge in edges:
        if edge[0] == current and edge[1] not in path:
            search(path.copy() + [edge[1]])
        if edge[1] == current and edge[0] not in path:
            search(path.copy() + [edge[0]])


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]

    if M == 0:
        print(f"#{test_case} 1")
        continue

    distance = 0
    for i in range(1, N + 1):
        search([i])

    print(f"#{test_case} {distance}")
