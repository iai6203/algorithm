# 프로그래머스 - N으로 표현
#
# https://school.programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    DP = [set() for _ in range(9)]

    DP[0] = None
    DP[1] = set([N])

    if N == number:
        return 1

    for count in range(2, 9):
        # print(f"count={count}")

        DP[count].add(int(str(N) * count))

        i1 = 1
        i2 = count - 1
        while i1 <= count - 1 and i2 >= 1:
            # print(f"DP[{i1}] 연산 DP[{i2}]")

            for n1 in DP[i1]:
                for n2 in DP[i2]:
                    DP[count].add(n1 + n2)
                    DP[count].add(n1 - n2)
                    DP[count].add(n1 * n2)
                    if n2 != 0: DP[count].add(n1 // n2)

            i1 += 1
            i2 -= 1

        # print(DP[count])

        if number in DP[count]:
            return count

        # print("------")

    return -1
