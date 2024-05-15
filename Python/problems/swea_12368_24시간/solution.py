# import sys
#
# sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    hours = A + B
    answer = hours % 24

    print(f"#{test_case} {answer}")
