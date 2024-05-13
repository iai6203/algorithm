import sys


sys.stdin = open("input.txt", "r")


def solution():
    TC = int(input())

    for test_case in range(1, TC + 1):
        N, M = map(int, input().split())
        S = input().split()
        T = input().split()
        Q = int(input())
        Y = [int(input()) for _ in range(0, Q)]

        answers = []
        for year in Y:
            s_index = (year - 1) % len(S)
            y_index = (year - 1) % len(T)

            answers.append(S[s_index] + T[y_index])

        answer = " ".join(answers)

        print(f"#{test_case} {answer}")


solution()
