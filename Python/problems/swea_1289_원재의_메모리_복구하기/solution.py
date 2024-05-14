# import sys
#
# sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    mem = list(input())
    cur = ['0'] * len(mem)

    cnt = 0
    cv = None
    for i in range(len(mem)):
        if cv is None and mem[i] != cur[i]:
            cnt += 1
            cv = mem[i]
            cur[i] = cv
        elif cv is not None and mem[i] != cv:
            cnt += 1
            cv = mem[i]
            cur[i] = cv

    print(f"#{test_case} {cnt}")
