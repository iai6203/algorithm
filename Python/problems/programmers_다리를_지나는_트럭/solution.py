# 프로그래머스 - 다리를 지나는 트럭
#
# https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque


def solution(bridge_length, weight, truck_weights):
    start = deque(truck_weights)
    end = 0
    bridge = deque([0] * bridge_length)

    sec = 0
    cur_w = 0
    while end < len(truck_weights):
        out_w = bridge.popleft()
        if out_w != 0:
            cur_w -= out_w
            end += 1

        if start and cur_w + start[0] <= weight:
            in_w = start.popleft()
            cur_w += in_w
            bridge.append(in_w)
        else:
            bridge.append(0)

        sec += 1

    return sec
