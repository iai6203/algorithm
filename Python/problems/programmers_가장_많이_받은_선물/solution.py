# 프로그래머스 - 가장 많이 받은 선물
#
# https://school.programmers.co.kr/learn/courses/30/lessons/258712

def solution(friends, gifts):
    count = [0 for _ in range(len(friends))]

    position = {}
    profiles = {}
    for idx, friend in enumerate(friends):
        position[friend] = idx
        profiles[idx] = {"give": 0, "take": 0}

    table = [[0 for _ in range(len(friends))] for _ in range(len(friends))]

    for gift in gifts:
        frm, to = gift.split()

        table[position[frm]][position[to]] += 1
        profiles[position[frm]]["give"] += 1
        profiles[position[to]]["take"] += 1

    for i, friend in enumerate(table):
        for j in range(len(friends)):
            if i == j: continue

            # 내가 더 많이 선물한 경우
            if table[i][j] > table[j][i]:
                count[i] += 1

            # 선물 개수가 같아 지수를 비교하는 경우
            if table[i][j] == table[j][i]:
                if profiles[i]["give"] - profiles[i]["take"] > profiles[j]["give"] - profiles[j]["take"]:
                    count[i] += 1

    return max(count)
