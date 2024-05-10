import sys
import copy

sys.stdin = open("input.txt", "r")


def next_list():
    li = []
    for i in range(0, 9):
        li.append(list(map(int, input().split())))
    return li


def extract_square(sudoku, start_row_index, start_col_index):
    copy_sudoku = copy.copy(sudoku)

    numbers = []
    for i in range(0, 3):
        for j in range(0, 3):
            numbers.append(copy_sudoku[start_row_index + i][start_col_index + j])

    return numbers


def check_row(sudoku):
    is_valid = True
    for row in range(0, 9):
        if not validate(sudoku[row]):
            is_valid = False
            break
    return is_valid


def check_col(sudoku):
    is_valid = True
    for col in range(0, 9):
        numbers = []
        for row in range(0, 9):
            numbers.append(sudoku[row][col])
        if not validate(numbers):
            is_valid = False
            break
    return is_valid


def check_square(sudoku):
    is_valid = True
    for i in range(0, 3):
        for j in range(0, 3):
            if not validate(extract_square(sudoku, i * 3, j * 3)):
                is_valid = False
                break

    return is_valid


def validate(numbers):
    copy_numbers = copy.copy(numbers)
    copy_numbers.sort()

    is_valid = True
    for i in range(0, 9):
        if not copy_numbers[i] == i + 1:
            is_valid = False
            break

    return is_valid


def solution():
    T = int(input())

    for test_case in range(1, T + 1):
        sudoku = next_list()
        if not check_row(sudoku):
            # print(f"특정 ROW에 오류가 있습니다.")
            print(f"#{test_case} 0")
            continue
        if not check_col(sudoku):
            # print(f"특정 COL에 오류가 있습니다.")
            print(f"#{test_case} 0")
            continue
        if not check_square(sudoku):
            # print(f"특정 SQUARE에 오류가 있습니다.")
            print(f"#{test_case} 0")
            continue

        print(f"#{test_case} 1")


solution()
