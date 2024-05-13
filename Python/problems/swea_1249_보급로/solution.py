import sys
import heapq


sys.stdin = open("input.txt", "r")


def solution():
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())

        board = [list(map(int, input())) for _ in range(0, N)]
        check = [[float("inf") for _ in range(0, N)] for _ in range(0, N)]

        check[0][0] = 0

        queue = []
        heapq.heappush(queue, [0, [0, 0]])

        while len(queue) > 0:
            item_distance, item_position = heapq.heappop(queue)

            if item_distance > check[item_position[0]][item_position[1]]:
                continue

            adjacent_list = []
            if item_position[0] > 0:
                adjacent_list.append([item_position[0] - 1, item_position[1]])
            if item_position[0] < N - 1:
                adjacent_list.append([item_position[0] + 1, item_position[1]])
            if item_position[1] > 0:
                adjacent_list.append([item_position[0], item_position[1] - 1])
            if item_position[1] < N - 1:
                adjacent_list.append([item_position[0], item_position[1] + 1])

            for adjacent_position in adjacent_list:
                distance = item_distance + board[adjacent_position[0]][adjacent_position[1]]

                if check[adjacent_position[0]][adjacent_position[1]] > distance:
                    check[adjacent_position[0]][adjacent_position[1]] = distance
                    heapq.heappush(queue, [distance, [adjacent_position[0], adjacent_position[1]]])

        print(f"#{test_case} {check[N - 1][N - 1]}")


solution()
