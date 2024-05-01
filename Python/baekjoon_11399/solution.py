# BAEKJOON 11399
#
# 링크 : https://www.acmicpc.net/problem/11399

N = int(input())
P_list = list(map(int, input().split(" ")))


def solution():
    P_list.sort()

    acc = [0] * N

    total = 0
    for i in range(0, N):
        if i == 0:
            acc[i] = P_list[i]
        else:
            acc[i] = acc[i - 1] + P_list[i]

        total += acc[i]

    print(total)


solution()
