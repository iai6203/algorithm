import sys

sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    a, b, c = list(map(int, input().split()))
    count = 0

    if not (b >= 2 and c >= 3):
        print(f"#{test_case} -1")
        continue

    if b >= c:
        count += b - c + 1
        b = c - 1
    if a >= b:
        count += a - b + 1
        a = b - 1

    print(f"#{test_case} {count}")
