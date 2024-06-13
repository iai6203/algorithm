# 프로그래머스 - 주식가격
#
# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    ans = [0] * len(prices)
    stack = []

    for c_i in range(len(prices)):
        if len(stack) == 0 or prices[c_i] >= prices[stack[-1]]:
            stack.append(c_i)
        else:
            while stack:
                if prices[c_i] < prices[stack[-1]]:
                    p_i = stack.pop()

                    ans[p_i] = c_i - p_i
                else:
                    break

            stack.append(c_i)

    for i in stack:
        ans[i] = len(prices) - i - 1

    return ans


solution([1, 2, 3, 2, 3])
