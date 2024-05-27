# 프로그래머스 - 멀리 뛰기
#
# https://school.programmers.co.kr/learn/courses/30/lessons/12914#

def solution(n):
    values = [0 for _ in range(max(3, n + 1))]
    values[1] = 1
    values[2] = 2

    if n <= 2:
        return values[n]

    for i in range(3, n + 1):
        values[i] = values[i - 2] + values[i - 1]

    return values[n] % 1234567
