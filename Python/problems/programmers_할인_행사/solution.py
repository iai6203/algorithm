# 프로그래머스 - 할인 행사
#
# https://school.programmers.co.kr/learn/courses/30/lessons/131127

def solution(want, number, discount):
    answer = 0

    for i in range(0, (len(discount) - 10) + 1):
        li = discount[i:i + 10]

        v = True
        for w, n in zip(want, number):
            if li.count(w) != n:
                v = False
                break

        if v is True:
            answer += 1

    return answer
