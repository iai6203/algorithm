import sys

sys.stdin = open("sample_input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    buildings = list(map(int, input().split()))

    total = 0
    for i in range(2, len(buildings) - 2):
        building = buildings[i]

        left_max = max(buildings[i - 1], buildings[i - 2])
        right_max = max(buildings[i + 1], buildings[i + 2])
        total_max = max(left_max, right_max)

        if building > total_max:
            total += building - total_max

    print(f"#{test_case} {total}")
