import sys

sys.stdin = open("input.txt", "r")


T = int(input())

numbers = [2, 3, 5, 7, 11]


for test_case in range(1, T + 1):
    N = int(input())

    count = [0, 0, 0, 0, 0]
    current = N
    while True:
        for i in range(len(numbers)):
            if current % numbers[i] == 0:
                current = int(current / numbers[i])
                count[i] += 1
                break

        if current == 1:
            break

    answer = ""
    for i, number in enumerate(count):
        if i > 0:
            answer += " "
        answer += str(number)

    print(f"#{test_case} {answer}")
