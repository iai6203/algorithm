# 프로그래머스 - 숫자 게임
#
# https://school.programmers.co.kr/learn/courses/30/lessons/12987

def solution(A, B):
    A.sort()
    B.sort()

    match = []
    start_i = 0
    visit = [False for _ in range(len(B))]

    for a_n in A:
        for b_i in range(start_i, len(B)):
            if a_n < B[b_i] and visit[b_i] == False:
                match.append((a_n, B[b_i]))
                start_i = b_i
                visit[b_i] = True
                break

    return len(match)
