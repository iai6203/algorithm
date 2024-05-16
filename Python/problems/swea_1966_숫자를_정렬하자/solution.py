import sys

sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    sorted_numbers = map(str, sorted(numbers))

    print(f"#{test_case} {' '.join(sorted_numbers)}")
