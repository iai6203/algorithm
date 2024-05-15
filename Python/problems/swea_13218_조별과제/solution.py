import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    group_cnt = N // 3

    print(f"#{test_case} {group_cnt}")
