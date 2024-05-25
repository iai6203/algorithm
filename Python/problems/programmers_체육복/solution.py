# 프로그래머스 - 체육복
#
# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0

    status = [None] + [1 for _ in range(n)]
    for item in lost:
        status[item] -= 1
    for item in reserve:
        status[item] += 1

    for i in range(1, n + 1):
        if status[i] == 1:
            continue

        if i == 1 and status[i] == 2 and status[i + 1] == 0:
            status[i] -= 1
            status[i + 1] += 1
            continue

        if status[i] == 2 and status[i - 1] == 0:
            status[i] -= 1
            status[i - 1] += 1
            continue

        if status[i] == 2 and (i + 1) < len(status) and status[i + 1] == 0:
            status[i] -= 1
            status[i + 1] += 1
            continue

    for i in range(len(status)):
        if status[i] == 1 or status[i] == 2:
            answer += 1

    return answer
