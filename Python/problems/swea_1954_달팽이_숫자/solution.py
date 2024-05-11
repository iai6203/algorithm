import sys

sys.stdin = open("input.txt", "r")


def solution():
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())
        if N == 1:
            print(f"#{test_case}")
            print("1")
            continue

        number = 1
        row = 0
        col = 0
        direction = [0, 1]
        wall = {"t": 0, "l": 0, "r": N - 1, "b": N - 1}

        board = [[0 for _ in range(0, N)] for _ in range(0, N)]

        while True:
            if board[row][col] != 0:
                break

            board[row][col] = number

            # Right
            if (direction[0] == 0 and direction[1] == 1) and (col == wall["r"]):
                wall["t"] += 1
                direction = [1, 0]
            # Down
            elif (direction[0] == 1 and direction[1] == 0) and (row == wall["b"]):
                wall["r"] -= 1
                direction = [0, -1]
            # Left
            elif (direction[0] == 0 and direction[1] == -1) and (col == wall["l"]):
                wall["b"] -= 1
                direction = [-1, 0]
            # Up
            elif (direction[0] == -1 and direction[1] == 0) and (row == wall["t"]):
                wall["l"] += 1
                direction = [0, 1]

            number += 1
            row += direction[0]
            col += direction[1]

        print(f"#{test_case}")
        for i in range(0, len(board)):
            print(" ".join(map(str, board[i])))


solution()
