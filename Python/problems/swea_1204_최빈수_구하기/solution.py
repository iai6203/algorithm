import sys


sys.stdin = open("input.txt", "r")


def find(scores):
    counter = {}
    for score in scores:
        if not counter.get(score):
            counter[score] = 0

        counter[score] += 1

    max_value = (0, 0)
    for key, value in counter.items():
        if value > max_value[1]:
            max_value = (key, value)

    return max_value[0]


def solution():
    T = int(input())

    for test_case in range(1, T + 1):
        case_no = int(input())
        scores = list(map(int, input().split()))
        number = find(scores)

        print(f"#{case_no} {number}")


solution()
