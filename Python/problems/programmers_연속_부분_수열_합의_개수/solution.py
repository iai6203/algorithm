# 프로그래머스 - 연속 부분 수열 합의 개수
#
# https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
    sums = set()

    for l in range(1, len(elements) + 1):
        for i in range(len(elements)):
            start_i = i
            end_i = (i + l) % len(elements)

            if start_i < end_i:
                sums.add(sum(elements[start_i:end_i]))
            else:
                sums.add(sum(elements[start_i:] + elements[:end_i]))

    return len(sums)
