import sys

sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split()))for _ in range(N)]

    count = 0
    for r in range(N):
        for c in range(N):
            if puzzle[r][c] == 0:
                continue

            # 가로 조건
            if c == 0 or (c > 0 and puzzle[r][c - 1] == 0) and c + K <= N:
                is_valid = True
                for dc in range(K):
                    if puzzle[r][c + dc] == 0:
                        is_valid = False
                        break
                if c + K < N and puzzle[r][c + K] == 1:
                    is_valid = False

                if is_valid:
                    count += 1

            # 세로 조건
            if r == 0 or (r > 0 and puzzle[r - 1][c] == 0) and r + K <= N:
                is_valid = True
                for dr in range(K):
                    if puzzle[r + dr][c] == 0:
                        is_valid = False
                        break
                if r + K < N and puzzle[r + K][c] == 1:
                    is_valid = False

                if is_valid:
                    count += 1

    print(f"#{test_case} {count}")
