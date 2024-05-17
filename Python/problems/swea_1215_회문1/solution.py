import sys
import math

sys.stdin = open("input.txt", "r")


def is_palindrome(s):
    flag = True
    middle_index = math.floor(len(s))
    for i in range(middle_index):
        if s[i] != s[-1 - i]:
            flag = False
            break
    return flag


for test_case in range(1, 11):
    N = int(input())
    word = [list(input()) for _ in range(8)]

    count = 0

    for row in range(8):
        for col in range(8):
            horizontal_word = ""
            vertical_word = ""

            is_horizontal_available = col + N <= 8
            is_vertical_available = row + N <= 8
            for i in range(N):
                if is_horizontal_available:
                    horizontal_word += word[row][col + i]
                if is_vertical_available:
                    vertical_word += word[row + i][col]

            if len(horizontal_word) == N and is_palindrome(horizontal_word):
                count += 1
            if len(vertical_word) == N and is_palindrome(vertical_word):
                count += 1

    print(f"#{test_case} {count}")
