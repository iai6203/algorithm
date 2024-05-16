import sys

sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    a, b, c = map(int, input().split())

    answer = 0.0
    if (b - a) == (c - b):
        pass
    else:
        answer = abs(((b - a) - (c - b)) / 2)

    print(f"#{test_case} {answer}")
