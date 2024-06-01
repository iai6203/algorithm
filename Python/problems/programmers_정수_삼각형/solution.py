# 프로그래머스 - 정수 삼각형
#
# https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    answer = 0

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][0]
                continue

            if j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
                continue

            triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
            answer = max(answer, triangle[i][j])

    return answer
