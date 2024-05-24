# 프로그래머스 - 야근 지수
#
# https://school.programmers.co.kr/learn/courses/30/lessons/12927

def solution(n, works):
    answer = 0

    work_count = 0
    while work_count < n:
        MAX = max(works)

        if MAX == 0:
            break

        for i, work in enumerate(works):
            if work_count == n:
                break

            if work > 0 and work == MAX:
                works[i] -= 1
                work_count += 1

    for work in works:
        answer += work ** 2

    return answer
