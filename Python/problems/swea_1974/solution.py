import sys

sys.stdin = open("input.txt", "r")

T = int(input())
X = 9
Y = 9


def check(numbers):
    result = True
    copy_numbers = numbers.copy()
    copy_numbers.sort()

    for i in range(0, 9):
        if copy_numbers[i] != i + 1:
            result = False
            break

    return result


def extract_square(board, start_row_index, start_col_index):
    numbers = []
    for i in range(start_row_index, start_row_index + 3):
        for j in range(start_col_index, start_col_index + 3):
            numbers.append(board[i][j])
    return numbers


def solution():
    for test_case in range(1, T + 1):
        result = True
        sudoku = []
        for i in range(0, Y):
            sudoku.append(list(map(int, input().split())))

        for row_index in range(0, Y):
            row = sudoku[row_index].copy()
            if not check(row):
                # print(f"가로 조건 불만족: {row}")
                result = False
                break

        if not result:
            print(f"#{test_case} 0")
            continue

        for col_index in range(0, X):
            col = []
            for i in range(0, Y):
                col.append(sudoku[i][col_index])

            if not check(col):
                # print(f"세로 조건 불만족: {col}")
                result = False
                break

        if not result:
            print(f"#{test_case} 0")
            continue

        for i in range(0, 3):
            for j in range(0, 3):
                numbers = extract_square(sudoku, i * 3, j * 3)
                if not check(numbers):
                    # print(f"정사각형 조건 불만족: {numbers}")
                    result = False

        if not result:
            print(f"#{test_case} 0")
            continue

        print(f"#{test_case} 1")


solution()
