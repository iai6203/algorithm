import sys

sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    numbers = set()
    i = 0
    while len(numbers) < 10:
        i += 1

        for char in list(str(N * i)):
            numbers.add(char)

    print(f"#{test_case} {N * i}")
