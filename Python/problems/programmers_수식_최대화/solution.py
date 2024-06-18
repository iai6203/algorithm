# 프로그래머스 - 2020 카카오 인턴신 - 수식 최대화
#
# https://school.programmers.co.kr/learn/courses/30/lessons/67257

import re


def permutation(n, r):
    ans = []

    def generate(chosen, checklist):
        if len(chosen) == r:
            ans.append(chosen.copy())
            return

        for i in range(len(n)):
            if checklist[i] == 0:
                chosen.append(n[i])
                checklist[i] = 1
                generate(chosen, checklist)
                chosen.pop()
                checklist[i] = 0

    generate([], [0] * len(n))

    return ans


def get_exp_list(s_list):
    exp_set = set()

    for s in s_list:
        if len(exp_set) == 3:
            break

        if s == "+" or s == "-" or s == "*":
            exp_set.add(s)

    return list(exp_set)


def calculate(arr, exp_priority):
    cur_arr = arr.copy()
    stack = []

    for exp in exp_priority:
        for s in cur_arr:
            if len(stack) == 0:
                stack.append(s)
                continue

            if stack[-1] == exp:
                stack.pop()
                n1 = int(stack.pop())
                n2 = int(s)

                if exp == "+":
                    stack.append(n1 + n2)
                elif exp == "-":
                    stack.append(n1 - n2)
                elif exp == "*":
                    stack.append(n1 * n2)
            else:
                stack.append(s)

        cur_arr = list(stack)
        stack = []

    return abs(cur_arr[0])


def solution(expression):
    ans = 0
    s_expression = re.split("([+\\-*])", expression)
    exp_list = get_exp_list(s_expression)

    for exp_priority in permutation(exp_list, len(exp_list)):
        ans = max(ans, calculate(s_expression, exp_priority))

    return ans


print(solution("100-200*300-500+20"))  # 60420
print(solution("50*6-3*2"))  # 300
