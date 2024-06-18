# 프로그래머스 - 순열 검사
#
# https://school.programmers.co.kr/learn/courses/18/lessons/1877

def solution(arr):
    max_num = max(arr)

    if len(arr) != max_num:
        return False

    checklist = [0] * (max_num + 1)
    checklist[0] = 1

    for n in arr:
        checklist[n] = 1

    return checklist.count(0) == 0
