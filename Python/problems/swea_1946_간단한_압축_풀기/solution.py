import sys

sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    q = []
    for i in range(N):
        inputs = input().split()
        char, count = inputs[0], int(inputs[1])

        for j in range(count):
            q.append(char)

    print(f"#{test_case}")
    while len(q) > 0:
        if len(q) > 10:
            line = "".join(q[:10])
            q = q[10:]
            print(line)
        else:
            line = "".join(q)
            q = []
            print(line)
