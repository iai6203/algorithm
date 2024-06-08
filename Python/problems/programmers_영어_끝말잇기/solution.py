# 프로그래머스 - 영어 끝말잇기
#
# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    d = {}
    s = []

    for i, w in enumerate(words):
        if (s and w[0] != s[-1][-1]) or (w in d):
            return [(i % n) + 1, (i // n) + 1]

        d[w] = True
        s.append(w)

    return [0, 0]

