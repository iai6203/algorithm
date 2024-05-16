import sys

sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    commands = [input().split() for _ in range(N)]

    distance = 0
    speed = 0
    while len(commands) > 0:
        command = commands.pop(0)
        if command[0] == "0":
            pass
        elif command[0] == "1":
            speed += int(command[1])
        elif command[0] == "2":
            speed -= int(command[1])
            if speed < 0:
                speed = 0

        distance += speed

    print(f"#{test_case} {distance}")
