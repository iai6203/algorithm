# 프로그래머스 - 올바른 괄호
#
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []

    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
            continue

        if s[i] == ")":
            if len(stack) == 0:
                return False

            stack.pop()

    if len(stack) > 0:
        return False

    return True
