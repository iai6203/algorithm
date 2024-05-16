# import sys
#
# sys.stdin = open("input.txt", "r")


T = int(input())

triangle = [[1]]

for row in range(1, 10):
    rows = []
    for col in range(row + 1):
        if col == 0 or col == row:
            rows.append(1)
        else:
            rows.append(triangle[row - 1][col - 1] + triangle[row - 1][col])
    triangle.append(rows)


for test_case in range(1, T + 1):
    N = int(input())

    print(f"#{test_case}")
    for row in range(N):
        print(' '.join(list(map(str, triangle[row]))))
