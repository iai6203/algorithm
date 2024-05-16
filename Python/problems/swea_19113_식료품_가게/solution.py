import sys

sys.stdin = open("input.txt", "r")


TC = int(input())

for test_case in range(1, TC + 1):
    N = int(input())
    candidates = list(map(int, input().split()))

    sale_prices = []
    while len(candidates) > 0:
        price = candidates.pop(0)
        original_price = price / 0.75

        for idx, candidate in enumerate(candidates):
            if candidate == original_price:
                sale_prices.append(price)
                candidates.pop(idx)
                break

    answer = " ".join(list(map(str, sale_prices)))

    print(f"#{test_case} {answer}")
