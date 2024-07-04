# 프로그래머스 - 야근 지수
#
# https://school.programmers.co.kr/learn/courses/30/lessons/12927

import heapq


def solution(n, works):
    pq = []

    for work in works:
        heapq.heappush(pq, (-work, work))

    while n > 0:
        priority, value = heapq.heappop(pq)
        next_value = value - 1
        if next_value < 0:
            next_value = 0

        heapq.heappush(pq, (-next_value, next_value))
        n -= 1

    return sum([value ** 2 for priority, value in pq])


print(solution(4, [4, 3, 3]))  # 12
print(solution(1, [2, 1, 2], ))  # 6
print(solution(3, [1, 1]))  # 0
