# 프로그래머스 - 네트워크
#
# https://school.programmers.co.kr/learn/courses/30/lessons/43162


import collections


def solution(n, computers):
    answer = 0

    tasks = collections.deque()
    connected = [False for _ in range(n)]

    while False in connected:
        for i in range(n):
            if connected[i] == False:
                tasks.append(i)
                break

        while len(tasks) > 0:
            i = tasks.popleft()

            connected[i] = True

            for j in range(n):
                if i != j and computers[i][j] == 1 and connected[j] == False:
                    tasks.append(j)

        answer += 1

    return answer
