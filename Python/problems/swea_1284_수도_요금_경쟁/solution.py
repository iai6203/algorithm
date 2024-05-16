import sys

sys.stdin = open("input.txt", "r")


T = int(input())


for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())

    fee_a = W * P
    fee_b = Q
    if W > R:
        fee_b += S * (W - R)

    print(f"#{test_case} {min(fee_a, fee_b)}")
