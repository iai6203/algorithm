import sys
import math


sys.stdin = open("input.txt", "r")


def solution():
    TC = int(input())

    for test_case in range(1, TC + 1):
        N = int(input())
        S = input()

        if len(S) % 2 == 1:
            print(f"#{test_case} No")
            continue

        half = math.floor(len(S) / 2)
        head = S[:half]
        tail = S[half:]

        if head != tail:
            print(f"#{test_case} No")
            continue

        print(f"#{test_case} Yes")


solution()
