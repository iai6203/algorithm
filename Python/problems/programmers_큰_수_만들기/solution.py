# 프로그래머스 - 큰 수 만들기
#
# https://school.programmers.co.kr/learn/courses/30/lessons/42883

import collections


def solution(number, k):
    stack = collections.deque()

    for n in number:
        while k > 0 and len(stack) > 0 and int(n) > int(stack[-1]):
            stack.pop()
            k -= 1

        stack.append(n)

    while not k == 0:
        stack.pop()
        k -= 1

    return "".join(stack)
