import sys

sys.stdin = open("input.txt", "r")


T = int(input())

money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for test_case in range(1, T + 1):
    N = int(input())

    pay_money_list = [0] * 8

    for i in range(len(money_list)):
        cnt = N // money_list[i]

        pay_money_list[i] = cnt
        N -= money_list[i] * cnt

        if N == 0:
            break

    print(f"#{test_case}")
    print(' '.join(list(map(str, pay_money_list))))
