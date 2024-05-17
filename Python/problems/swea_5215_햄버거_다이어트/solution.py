import sys

sys.stdin = open("input.txt", "r")


T = int(input())


def search(i, score, kcal):
    global max_score

    if kcal > L:
        return

    max_score = max(max_score, score)

    if i == N:
        return

    search(i + 1, score + ingredients[i][0], kcal + ingredients[i][1])
    search(i + 1, score, kcal)


for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    ingredients = [list(map(int, input().split())) for _ in range(N)]

    max_score = 0
    search(0, 0, 0)

    print(f"#{test_case} {max_score}")
