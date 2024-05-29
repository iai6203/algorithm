# 프로그래머스 - 숫자의 표현
#
# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0

    for st in range(1, n + 1):
        tot = 0

        if st == n:
            answer += 1
            continue

        for cn in range(st, n + 1):
            if tot == n:
                answer += 1
                break

            if tot > n:
                break

            tot += cn

    return answer
