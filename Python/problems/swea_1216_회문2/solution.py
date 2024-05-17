import sys
import math

sys.stdin = open("input.txt", "r")


T = 10
SIZE = 100


def is_palindrome(s):
    flag = True
    middle_idx = int(math.floor(len(s) / 2))
    for i in range(middle_idx):
        if s[i] != s[-1 - i]:
            flag = False
            break
    return flag


def search(length):
    flag = False

    for row in range(SIZE):
        if flag:
            break

        for col in range(SIZE):
            horizontal = ""
            vertical = ""

            is_horizontal_available = col + length <= SIZE
            is_vertical_available = row + length <= SIZE
            for idx in range(length):
                if is_horizontal_available:
                    horizontal += chars[row][col + idx]
                if is_vertical_available:
                    vertical += chars[row + idx][col]

            if len(horizontal) == length and is_palindrome(horizontal):
                flag = True
                break
            if len(vertical) == length and is_palindrome(vertical):
                flag = True
                break
    return flag


for _ in range(1, T + 1):
    case_no = int(input())
    chars = [list(input()) for _ in range(SIZE)]

    answer = 1
    for i in range(2, SIZE):
        if search(i):
            answer = i

    print(f"#{case_no} {answer}")
