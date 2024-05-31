# 프로그래머스 - 카펫
#
# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    row = 1
    col = 1

    while True:
        y = (row - 2) * (col - 2)
        b = (row * col) - y

        if y == yellow and b == brown:
            break

        if row == col:
            row += 1
            col = 1
        else:
            col += 1

    return [row, col]
