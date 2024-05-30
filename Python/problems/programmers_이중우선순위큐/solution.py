# 프로그래머스 - 이중우선순위큐
#
# https://school.programmers.co.kr/learn/courses/30/lessons/42628


import heapq


def solution(operations):
    min_heap = []
    max_heap = []

    for operation in operations:
        w, v = operation.split()

        int_v = int(v)

        if w == "I":
            heapq.heappush(min_heap, int_v)
            heapq.heappush(max_heap, -int_v)
        elif w == "D" and len(min_heap) > 0:
            if v == "1":
                rm = heapq.heappop(max_heap)
                min_heap.remove(rm * -1)
            else:
                rm = heapq.heappop(min_heap)
                max_heap.remove(rm * -1)

    if len(min_heap) == 0:
        return [0, 0]
    else:
        return [
            heapq.heappop(max_heap) * -1,
            heapq.heappop(min_heap),
        ]
