# BAEKJOON 1920
#
# 링크 : https://www.acmicpc.net/problem/1920

N = int(input())
N_list = list(map(int, input().split(" ")))
M = int(input())
M_list = list(map(int, input().split(" ")))


def binary_search(target, start, end):
    if start > end:
        return 0

    middle_index = (start + end) // 2

    if target == N_list[middle_index]:
        return 1
    elif target < N_list[middle_index]:
        return binary_search(target, start, middle_index - 1)
    elif target > N_list[middle_index]:
        return binary_search(target, middle_index + 1, end)
    else:
        return 0


def solution():
    N_list.sort()
    for i in range(0, M):
        print(binary_search(M_list[i], 0, N - 1))


solution()
