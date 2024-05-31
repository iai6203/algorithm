# 프로그래머스 - 짝지어 제거하기
#
# https://school.programmers.co.kr/learn/courses/30/lessons/12973

import collections


def solution(s):
    stack = collections.deque()

    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
            continue

        before = stack.pop()

        if before == s[i]:
            continue
        else:
            stack.append(before)
            stack.append(s[i])

    if len(stack) == 0:
        return 1
    else:
        return 0
