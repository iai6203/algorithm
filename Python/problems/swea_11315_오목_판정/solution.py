import sys

sys.stdin = open("input.txt", "r")


def is_available(row, col, v_row, v_col):
    flag = False
    count = 0

    current_row = row
    current_col = col
    while 0 <= current_row < N and 0 <= current_col < N:
        if game[current_row][current_col] == "o":
            count += 1
        else:
            count = 0

        if count == 5:
            flag = True
            break

        current_row += v_row
        current_col += v_col

    return flag


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    game = [list(input()) for _ in range(N)]

    flag = False

    for row in range(N):
        if is_available(row, 0, 0, 1) or is_available(row, 0, 1, 1) or is_available(row, N - 1, 1, -1):
            flag = True
            break
    for col in range(N):
        if is_available(0, col, 1, 0) or is_available(0, col, 1, 1) or is_available(0, col, 1, -1):
            flag = True
            break

    if flag:
        print(f"#{test_case} YES")
        continue

    print(f"#{test_case} NO")
