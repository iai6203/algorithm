import sys


sys.stdin = open("input.txt", "r")


def solution():
    T = int(input())

    for test_case in range(1, T + 1):
        N, M = map(int, input().split())
        board = [list(map(int, input().split())) for i in range(0, N)]

        total_max = 0
        for i in range(0, N - M + 1):
            for j in range(0, N - M + 1):

                total = 0
                for row in range(i, i + M):
                    for col in range(j, j + M):
                        total += board[row][col]
                total_max = max(total_max, total)

        print(f"#{test_case} {total_max}")


solution()
