import sys


sys.stdin = open("input.txt", "r")


def solution():
    T = 10

    for test_case in range(1, T + 1):
        dump = int(input())
        boxes = list(map(int, input().split()))

        current_dump = 0
        while current_dump < dump:
            max_index = 0
            min_index = 0

            for i in range(1, len(boxes)):
                if boxes[i] > boxes[max_index]:
                    max_index = i
                if boxes[i] < boxes[min_index]:
                    min_index = i

            boxes[max_index] -= 1
            boxes[min_index] += 1
            current_dump += 1

        print(f"#{test_case} {max(boxes) - min(boxes)}")


solution()
