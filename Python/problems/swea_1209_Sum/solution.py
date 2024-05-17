# import sys

# sys.stdin = open("input.txt", "r")


T = 10
SIZE = 100

for test_case in range(1, T + 1):
    case_no = int(input())
    numbers = [list(map(int, input().split())) for _ in range(SIZE)]

    row_sums = [0] * SIZE
    col_sums = [0] * SIZE
    from_top_left = 0
    from_top_right = 0

    max_number = 0
    for row in range(SIZE):
        for col in range(SIZE):
            row_sums[row] += numbers[row][col]
            col_sums[col] += numbers[row][col]

            if abs(row) == abs(col):
                from_top_left += numbers[row][col]
            if abs(row) == abs(col - 99):
                from_top_right += numbers[row][col]

    answer = max(max(row_sums), max(col_sums), from_top_left, from_top_right)

    print(f"#{test_case} {answer}")
