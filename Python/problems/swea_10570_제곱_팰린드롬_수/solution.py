# import sys
import math

# sys.stdin = open("input.txt", "r")


def is_palindrome(s):
    f = True
    for i in range(len(s) // 2):
        if s[i] != s[-1 - i]:
            f = False
            break
    return f


# MAIN
TC = int(input())


for test_case in range(1, TC + 1):
    A, B = map(int, input().split())

    cnt = 0
    for n in range(A, B + 1):
        sqrt = math.sqrt(n)

        if sqrt != int(sqrt):
            continue
        sqrt = int(sqrt)

        if not is_palindrome(str(n)):
            continue

        if not is_palindrome(str(sqrt)):
            continue

        cnt += 1

    print(f"#{test_case} {cnt}")
