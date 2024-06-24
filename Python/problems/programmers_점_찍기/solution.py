# 프로그래머스 - 점 찍기
#
# https://school.programmers.co.kr/learn/courses/30/lessons/140107

import math


def solution(k, d):
    ans = 0

    for x in range(0, d + 1, k):
        y = int(math.sqrt((d ** 2) - (x ** 2)))

        ans += (y // k) + 1

    return ans


print(solution(2, 4))  # 6
print(solution(1, 5))  # 26
