# 3  => 3
# 4  =>
# 5  => 5
# 6  => 3, 3
# 7  =>
# 8  => 5, 3
# 9  => 3, 3, 3
# 10 => 5, 5
# 11 => 5, 3, 3
# 12 => 3, 3, 3, 3
# 13 => 5, 5, 3
# 14 => 5, 3, 3, 3
# 15 => 5, 5, 5
# 16 => 5, 5, 3, 3
# 17 => 5, 3, 3, 3, 3
# 18 => 5, 5, 5, 3
# 19 => 5, 5, 3, 3, 3
# 20 => 5, 5, 5, 5

def solution(n):
    cache = [0] * (max(n + 1, 5))
    cache[3] = 1
    cache[4] = -1

    for i in range(5, n + 1):
        if i % 5 == 0:
            cache[i] = int(i / 5)
        elif cache[i - 3] == -1:
            cache[i] = -1
        else:
            cache[i] = cache[i - 3] + 1

    return cache[n]


n = int(input())
answer = solution(n)
print(answer)
