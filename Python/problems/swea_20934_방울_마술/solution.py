import sys


sys.stdin = open("input.txt", "r")


def solution():
    T = int(input())

    for test_case in range(1, T + 1):
        S, K = input().split()
        position = S.find("o")
        queue = [[position, 0]]
        count = [0] * 3

        while len(queue) > 0:
            current_position, current_count = queue.pop(0)

            if current_count == int(K):
                count[current_position] += 1
                continue

            if current_position == 0:
                queue.append([1, current_count + 1])
            if current_position == 1:
                queue.append([0, current_count + 1])
            if current_position == 2:
                queue.append([1, current_count + 1])

        max_position = 0
        max_count = count[0]
        for i in range(1, len(count)):
            if count[i] > max_count:
                max_position = i
                max_count = count[i]

        print(f"#{test_case} {max_position}")


solution()
