# 프로그래머스 - 최고의 집합
#
# https://school.programmers.co.kr/learn/courses/30/lessons/12938

import math


def solution(n, s):
    if n > s:
        return [-1]

    middle = math.floor(s / n)

    total = middle * n
    combination = [middle for _ in range(n)]

    i = 0
    while total < s:
        combination[-1 - i] += 1
        total += 1
        i += 1

    return combination
