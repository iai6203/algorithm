# 프로그래머스 - 소수 찾기
#
# https://school.programmers.co.kr/learn/courses/30/lessons/42839

import math


def permutation(n, r):
    ans = []

    def generate(chosen, checklist):
        if len(chosen) == r:
            ans.append(chosen.copy())
            return

        for i in range(len(n)):
            if checklist[i] == 1:
                continue

            chosen.append(n[i])
            checklist[i] = 1
            generate(chosen, checklist)
            chosen.pop()
            checklist[i] = 0

    generate([], [0] * len(n))

    return ans


def prime_numbers(candidates):
    ans = []
    max_candidate = max(candidates)

    primes = [1 for _ in range(max_candidate + 1)]
    primes[0] = 0
    primes[1] = 0

    for i in range(2, int(math.sqrt(max_candidate)) + 1):
        if primes[i] == 1:
            j = 2

            while i * j <= max_candidate:
                primes[i * j] = 0
                j += 1

    for candidate in candidates:
        if primes[candidate] == 1:
            ans.append(candidate)

    return ans


def solution(s):
    numbers = list(s)
    candidates = set()

    for i in range(len(numbers)):
        for n_arr in permutation(numbers, i + 1):
            candidates.add(int("".join(n_arr)))

    primes = prime_numbers(candidates)

    return len(primes)
