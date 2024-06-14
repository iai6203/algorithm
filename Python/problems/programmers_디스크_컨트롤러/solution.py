# 프로그래머스 - 디스크 컨트롤러
#
# https://school.programmers.co.kr/learn/courses/30/lessons/42627

import heapq


def solution(jobs):
    # 현재 시각(초)
    sec = 0
    # 각각의 작업의 요청부터 처리까지 걸린 시간의 총합
    duration = 0

    # 요청 시각 기준 힙
    entry_heap = [(job[0], job) for job in jobs]
    heapq.heapify(entry_heap)

    while entry_heap:
        # 현재 시각(초) 기준으로 가능한 작업들을 모두 조회
        candidates = []

        while entry_heap:
            candidate = heapq.heappop(entry_heap)

            if candidate[0] > sec:
                heapq.heappush(entry_heap, candidate)
                break
            else:
                heapq.heappush(candidates, (candidate[1][1], candidate[1]))

        # 현재 시각(초)을 기준으로 가능한 작업들이 없을 경우
        # -> 현재 시각(초)을 다음 작업이 들어오는 시각으로 맞추고 다음으로 스킵
        if not candidates:
            sec = entry_heap[0][0]
            continue

        # 현재 시각(초)을 기준으로 가능한 작업 중 가장 처리 시간이 적은 작업을 꺼내서 처리
        candidate = heapq.heappop(candidates)

        sec += candidate[0]
        duration += sec - candidate[1][0]

        for c in candidates:
            heapq.heappush(entry_heap, (c[1][0], c[1]))

    return int(duration / len(jobs))
