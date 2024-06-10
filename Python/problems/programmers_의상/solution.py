# 프로그래머스 - 의상
#
# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    dic = {}

    for name, category in clothes:
        if category not in dic:
            dic[category] = 0

        dic[category] += 1

    answer = 1
    for v in dic.values():
        answer *= v + 1
    answer -= 1

    return answer
