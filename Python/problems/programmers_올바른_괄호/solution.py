# 프로그래머스 - 올바른 괄호
#
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

import collections


def solution(s):
    q = collections.deque()

    for i in range(len(s)):
        if s[i] == "(" or s[i] == ")":
            q.append(s[i])

    # 괄호 개수가 홀수라면 잘못된 것!
    if len(q) % 2 == 1:
        return False

    stack = []
    while q:
        s1 = q.popleft()

        if s1 == "(":
            stack.append(s1)
            continue

        if s1 == ")":
            if len(stack) == 0:
                return False

            stack.pop()

    if len(stack) > 0:
        return False

    return True
