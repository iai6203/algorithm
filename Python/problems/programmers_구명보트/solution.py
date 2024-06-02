# 프로그래머스 - 구명보트
#
# https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    people.sort()

    boat = 0
    left_index = 0
    right_index = len(people) - 1

    while left_index < right_index:
        if people[left_index] + people[right_index] <= limit:
            boat += 1
            left_index += 1
            right_index -= 1
        else:
            boat += 1
            right_index -= 1

    if left_index == right_index: boat += 1

    return boat
