import sys

sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    guests = sorted(list(map(int, input().split())))

    flag = "Possible"
    second = 0
    product = 0
    sell = 0
    for guest in guests:
        if second != guest:
            second = guest
            product = (second // M) * K

        if not product >= sell + 1:
            flag = "Impossible"
            break

        sell += 1

    print(f"#{test_case} {flag}")
