def solution(n):
    cache = [0] * max(n + 1, 5 + 1)

    cache[1] = 1
    cache[2] = 1
    cache[3] = 1
    cache[4] = 2
    cache[5] = 2

    for i in range(6, n + 1):
        cache[i] = cache[i - 1] + cache[i - 5]

    print(cache[n])


case_count = int(input())

for i in range(1, case_count + 1):
    n = int(input())

    solution(n)
