import sys

sys.stdin = open("input.txt", "r")

# N극 (상단) / S극 (하단)
# 1 = N극(S극에 이끌림) / 2 = S극(N극에 이끌림)

T = 10


for test_case in range(1, T + 1):
    TABLE_SIZE = int(input())
    table = [list(map(int, input().split())) for _ in range(TABLE_SIZE)]

    count = 0

    for col in range(TABLE_SIZE):
        row = 0
        before = -1

        while row < TABLE_SIZE:
            current = table[row][col]
            if before == -1 and current == 1:
                before = current

            if before == 1 and current == 2:
                count += 1
                before = -1

            row += 1

    print(f"#{test_case} {count}")
