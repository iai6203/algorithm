# 프로그래머스 - 최소 직사각형
#
# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    w_candidates = []
    h_candidates = []

    for w, h in sizes:
        if w < h:
            w, h = h, w

        w_candidates.append(w)
        h_candidates.append(h)

    return max(w_candidates) * max(h_candidates)
