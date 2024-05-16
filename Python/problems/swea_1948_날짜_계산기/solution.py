import sys

sys.stdin = open("input.txt", "r")

T = int(input())
last_days = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for test_case in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())

    answer = None
    if m1 == m2:
        answer = (d2 - d1) + 1
    else:
        count = 0

        count += last_days[m1] - d1
        for m in range(m1 + 1, m2):
            count += last_days[m]
        count += d2
        answer = count + 1

    print(f"#{test_case} {answer}")
