import sys

sys.stdin = open("input.txt", "r")


def is_available(row, col, candidates):
    is_valid = True
    for candidates_row in range(len(candidates)):
        if col == candidates[candidates_row] or abs(row - candidates_row) == abs(col - candidates[candidates_row]):
            is_valid = False
            break
    return is_valid


def dfs(candidates):
    global count

    row = len(candidates)

    if len(candidates) == N:
        count += 1
        return

    for col in range(N):
        if is_available(row, col, candidates):
            dfs(candidates.copy() + [col])


#
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    count = 0
    for c in range(N):
        dfs([c])

    print(f"#{test_case} {count}")
