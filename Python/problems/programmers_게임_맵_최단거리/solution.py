# 프로그래머스 - 게임 맵 최단거리
#
# https://school.programmers.co.kr/learn/courses/30/lessons/1844


import collections


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    tasks = collections.deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    tasks.append((0, 0))

    while len(tasks) > 0:
        r, c = tasks.popleft()

        visited[r][c] = True

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1 and visited[nr][nc] is False:
                maps[nr][nc] = maps[r][c] + 1
                tasks.append((nr, nc))

    if maps[n - 1][m - 1] == 1:
        return -1
    else:
        return maps[n - 1][m - 1]
