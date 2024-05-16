import sys

sys.stdin = open("input.txt", "r")


def rotate(board):
    items = []
    for col in range(N):
        numbers = []
        for row in range(N):
            numbers.append(board[row][col])
        numbers.reverse()
        items.append(numbers)
    return items


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(input().split()) for _ in range(N)]

    deg_90 = rotate(board)
    deg_180 = rotate(deg_90)
    deg_270 = rotate(deg_180)

    print(f"#{test_case}")
    for i in range(N):
        line = "".join(deg_90[i]) + " " + "".join(deg_180[i]) + " " + "".join(deg_270[i])
        print(line)
