import sys

sys.stdin = open("input.txt", "r")


T = 10

for test_case in range(1, T + 1):
    case_no = int(input())
    numbers = list(map(int, input().split()))

    decrement = 1
    while numbers[len(numbers) - 1] > 0:
        number = numbers.pop(0)

        changed_number = number - decrement
        if changed_number < 0:
            changed_number = 0

        numbers.append(changed_number)

        decrement += 1
        if decrement > 5:
            decrement = 1

    answer = " ".join(list(map(str, numbers)))
    print(f"#{test_case} {answer}")
