# 동전 문제
#
# 지불해야 하는 값이 4720원 일 때 10원, 50원, 500원 동전으로 동전의 수가 가장 적게 지불하시오.
#   - 가장 큰 동전부터 최대한 지불해야 하는 값을 채우는 방식으로 구현 가능
#   - 탐욕 알고리즘으로 매순간 최적이라고 생각되는 경우를 선택하면 됨

def pay(price):
    coin = {
        "500": 0,
        "100": 0,
        "50": 0,
        "10": 0,
    }

    left = price
    while left > 0:
        if left > 500:
            coin["500"] += 1
            left -= 500
        elif left > 100:
            coin["100"] += 1
            left -= 100
        elif left > 50:
            coin["50"] += 1
            left -= 50
        else:
            coin["10"] += 1
            left -= 10

    print(f"500원: {coin['500']}")
    print(f"100원: {coin['100']}")
    print(f"50원: {coin['50']}")
    print(f"10원: {coin['10']}")


pay(4720)
