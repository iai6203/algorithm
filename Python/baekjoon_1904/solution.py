# 1 => 1 => 1
# 2 => 00 11 => 2
# 3 => 001 100 111 => 3
# 4 => 0000 0011 1001 1100 1111 => 5

def solution(n):
    cache = [0] * (max(n + 1, 2 + 1))

    cache[1] = 1
    cache[2] = 2

    for i in range(3, n + 1):
        cache[i] = (cache[i - 1] + cache[i - 2]) % 15746

    return cache[n]


n = int(input())
answer = solution(n)

print(answer)
