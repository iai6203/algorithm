# 프로그래머스 - 뒤에 있는 큰 수 찾기
#
# https://school.programmers.co.kr/learn/courses/30/lessons/154539


def solution(numbers):
    ans = [-1] * len(numbers)
    stack = []

    for index, number in enumerate(numbers):
        while stack and stack[-1][1] < number:
            prev_index, prev_number = stack.pop()
            ans[prev_index] = number

        stack.append((index, number))

    return ans


print(solution([2, 3, 3, 5]))  # [3, 5, 5, -1]
print(solution([9, 1, 5, 3, 6, 2]))  # [-1, 5, 6, 6, -1, -1]
