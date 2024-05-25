# 프로그래머스 - 카드 뭉치
#
# https://school.programmers.co.kr/learn/courses/30/lessons/159994

def solution(cards1, cards2, goal):
    c1_idx = 0
    c2_idx = 0

    for item in goal:
        if c1_idx < len(cards1) and item == cards1[c1_idx]:
            c1_idx += 1
            continue

        if c2_idx < len(cards2) and item == cards2[c2_idx]:
            c2_idx += 1
            continue

        return "No"

    return "Yes"
