# 프로그래머스 - 주식가격
#
# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = []

    for i in range(len(prices) - 1):
        sec = 0

        for j in range(i + 1, len(prices)):
            sec += 1

            if prices[i] > prices[j]:
                break

        answer.append(sec)

    answer.append(0)

    return answer
