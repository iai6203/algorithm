# 프로그래머스 - 예상 대진표
#
# https://school.programmers.co.kr/learn/courses/30/lessons/12985

import math


def solution(n, a, b):
    r = 1
    n1, n2 = sorted([a, b])

    while n1 + 1 != n2 or n1 % 2 == 0:
        n1 = math.ceil(n1 / 2)
        n2 = math.ceil(n2 / 2)

        r += 1

    return r
