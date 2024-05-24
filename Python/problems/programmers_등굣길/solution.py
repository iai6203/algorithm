# 프로그래머스 - 등굣길
#
# https://school.programmers.co.kr/learn/courses/30/lessons/42898

import collections


def my_solution(m, n, puddles):
    answer = 0
    dr = [0, 1]
    dc = [1, 0]

    map = [[1 for _ in range(m)] for _ in range(n)]
    for col, row in puddles:
        map[row - 1][col - 1] = 0

    stack = collections.deque()
    stack.append([0, 0, 0])

    min_length = float("inf")
    count = 0

    while stack:
        r, c, l = stack.popleft()

        if r == n - 1 and c == m - 1:
            if l < min_length:
                min_length = l
                count = 0

            if l == min_length:
                count += 1

            continue

        for i in range(2):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and map[nr][nc] == 1:
                stack.append([nr, nc, l + 1])

    return count % 1000000007


def best_solution(m, n, puddles):
    answer = 0

    map = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for col, row in puddles:
        map[row][col] = -1

    for row in range(1, n + 1):
        for col in range(1, m + 1):
            if row == 1 and col == 1:
                map[row][col] = 1
            elif map[row][col] == -1:
                map[row][col] = 0
            else:
                map[row][col] = map[row - 1][col] + map[row][col - 1]

    return map[n][m] % 1000000007

