# 프로그래머스 - K번째 수
#
# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []

    for command in commands:
        i, j, k = command

        answer.append(sorted(array[i - 1:j])[k - 1])

    return answer
