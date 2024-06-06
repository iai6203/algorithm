# 프로그래머스 - 정수를 나선형으로 배치하기
#
# https://school.programmers.co.kr/learn/courses/30/lessons/181832

def solution(n):
    arr = [[0 for _ in range(n)] for _ in range(n)]

    number = 1
    row, col = 0, 0
    min_row, min_col = 0, 0
    max_row, max_col = n - 1, n - 1
    d_row, d_col = 0, 1

    while min_row <= row <= max_row and min_col <= col <= max_col:
        arr[row][col] = number

        if col == max_col and (d_row == 0 and d_col == 1):
            min_row += 1
            d_row, d_col = 1, 0

        if row == max_row and (d_row == 1 and d_col == 0):
            max_col -= 1
            d_row, d_col = 0, -1

        if col == min_col and (d_row == 0 and d_col == -1):
            max_row -= 1
            d_row, d_col = -1, 0

        if row == min_row and (d_row == -1 and d_col == 0):
            min_col += 1
            d_row, d_col = 0, 1

        number += 1
        row += d_row
        col += d_col

    return arr
