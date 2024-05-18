import sys

sys.stdin = open("input.txt", "r")


# 1: B(흑돌), 2: W(백돌)


T = int(input())
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def place(row, col, color):
    global game

    game[row][col] = color

    for direction in directions:
        flag = False

        # find same color
        for i in range(N):
            check_row = row + (direction[0] + (direction[0] * i))
            check_col = col + (direction[1] + (direction[1] * i))

            if not (0 <= check_row < N and 0 <= check_col < N):
                break

            if game[check_row][check_col] == 0:
                break

            if game[check_row][check_col] == color:
                flag = True
                break

        # fill
        if flag:
            for i in range(N):
                check_row = row + (direction[0] + (direction[0] * i))
                check_col = col + (direction[1] + (direction[1] * i))

                if game[check_row][check_col] == color:
                    break

                game[check_row][check_col] = color


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    game = [[0 for _ in range(N)] for _ in range(N)]
    history = [list(map(int, input().split())) for _ in range(M)]

    center_index = int(N // 2)

    # 초기 배치
    game[center_index - 1][center_index - 1] = 2
    game[center_index - 1][center_index] = 1
    game[center_index][center_index - 1] = 1
    game[center_index][center_index] = 2

    # 시뮬레이션
    for item in history:
        place(item[0] - 1, item[1] - 1, item[2])

    # 숫자 세기
    black = 0
    white = 0
    for row in range(N):
        for col in range(N):
            if game[row][col] == 1:
                black += 1
            elif game[row][col] == 2:
                white += 1

    print(f"#{test_case} {black} {white}")
