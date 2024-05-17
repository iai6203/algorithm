# import sys

# sys.stdin = open("input.txt", "r")


T = int(input())


def search(i, total):
    global count

    if total > K:
        return

    if total == K:
        count += 1
        return

    if not i < N:
        return

    search(i + 1, total)
    search(i + 1, total + numbers[i])


for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    count = 0
    search(0, 0)

    print(f"#{test_case} {count}")
