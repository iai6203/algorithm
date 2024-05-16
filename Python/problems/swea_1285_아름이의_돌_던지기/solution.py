import sys

sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    throws = list(map(int, input().split()))

    closest = float("inf")
    for throw in throws:
        closest = min(closest, abs(throw))

    count = 0
    for throw in throws:
        if abs(throw) == closest:
            count += 1

    print(f"#{test_case} {closest} {count}")
