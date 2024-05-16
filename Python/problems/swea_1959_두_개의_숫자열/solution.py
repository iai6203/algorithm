import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    small_list = []
    big_list = []
    if len(A_list) > len(B_list):
        small_list = B_list
        big_list = A_list
    else:
        small_list = A_list
        big_list = B_list

    MAX = 0
    for position_index in range(abs(N - M) + 1):
        total = 0
        for i in range(len(small_list)):
            total += small_list[i] * big_list[i + position_index]
        MAX = max(MAX, total)

    print(f"#{test_case} {MAX}")
