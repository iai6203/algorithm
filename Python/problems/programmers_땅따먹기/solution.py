# 프로그래머스 - 땅따먹기
#
# https://school.programmers.co.kr/learn/courses/30/lessons/12913

from copy import deepcopy


def find_max(numbers, ignore_index):
    max_number = 0
    for i in range(4):
        if i != ignore_index:
            max_number = max(max_number, numbers[i])

    return max_number


def solution(land):
    numbers = deepcopy(land)
    max_floor = len(numbers) - 1

    for floor in range(1, max_floor + 1):
        for i in range(4):
            numbers[floor][i] += find_max(numbers[floor - 1], i)

    return max(numbers[max_floor])


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))  # 16
