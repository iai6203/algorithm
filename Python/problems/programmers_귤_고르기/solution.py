# 프로그래머스 - 귤 고르기
#
# https://school.programmers.co.kr/learn/courses/30/lessons/138476

import collections


def solution(k, tangerine):
    cnt = collections.Counter(tangerine)
    cnt = sorted(cnt.values(), reverse=True)

    i = 0
    box = 0
    while box < k:
        box += cnt[i]
        i += 1

    return i
