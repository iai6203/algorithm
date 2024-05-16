import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())

    total_h = h1 + h2
    total_m = m1 + m2

    hour = total_h + (total_m // 60)
    minute = total_m % 60

    if hour > 12:
        hour -= 12

    print(f"#{test_case} {hour} {minute}")
