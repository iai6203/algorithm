import sys


sys.stdin = open("input.txt", "r")


drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def dfs(r, c, distance, is_fixed):
    global MAX, visited

    visited[r][c] = 1
    MAX = max(MAX, distance)

    for dr, dc in drc:
        nr = r + dr
        nc = c + dc

        if not (0 <= nr < N and 0 <= nc < N) or visited[nr][nc] > 0:
            continue

        if visited[nr][nc] == 0 and mountain[nr][nc] < mountain[r][c]:
            dfs(nr, nc, distance + 1, is_fixed)
            visited[nr][nc] = 0
        elif not is_fixed and mountain[nr][nc] - K < mountain[r][c]:
            original = mountain[nr][nc]
            mountain[nr][nc] = mountain[r][c] - 1
            dfs(nr, nc, distance + 1, True)
            visited[nr][nc] = 0
            mountain[nr][nc] = original


# MAIN
T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]

    peek = 0
    for r in range(N):
        for c in range(N):
            peek = max(peek, mountain[r][c])

    MAX = 0
    for r in range(N):
        for c in range(N):
            if mountain[r][c] == peek:
                visited = [[0 for _ in range(N)] for _ in range(N)]
                dfs(r, c, 1, False)

    print(f"#{test_case} {MAX}")
