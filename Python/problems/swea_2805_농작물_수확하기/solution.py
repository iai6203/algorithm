import sys
import math

sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, list(input()))) for _ in range(N)]
    center_index = int(math.floor(N / 2))

    profit = 0
    length = 1
    direction = 1
    for row in range(N):
        profit += farm[row][center_index]

        if length > 1:
            for distance in range(1, length):
                profit += farm[row][center_index - distance]
                profit += farm[row][center_index + distance]

        if center_index + length == N:
            direction = -1

        length += direction

    print(f"#{test_case} {profit}")
