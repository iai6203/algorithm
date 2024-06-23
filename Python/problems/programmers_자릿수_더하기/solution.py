# 프로그래머스 - 자릿수 더하기
#
# https://school.programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    return sum(list(map(int, list(str(n)))))


print(solution(123))  # 6
print(solution(987))  # 24
