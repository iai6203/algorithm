# 프로그래머스 - 숫자 게임
#
# https://school.programmers.co.kr/learn/courses/30/lessons/12987

def solution(A, B):
    ans = 0

    A.sort(), B.sort()

    b_cursor = 0
    use = [0] * len(A)

    for a in A:
        for b_i in range(b_cursor, len(B)):
            if a < B[b_i] and use[b_i] == 0:
                ans += 1
                b_cursor = b_i + 1
                use[b_i] = 1
                break

    return ans


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))  # 3
print(solution([2, 2, 2, 2], [1, 1, 1, 1]))  # 0
