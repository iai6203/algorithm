# 프로그래머스 - 기능개발
#
# https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []

    i = 0
    d = 0
    c = 0

    while i < len(progresses):
        progress = progresses[i] + (speeds[i] * d)

        if progress >= 100:
            i += 1
            c += 1
            if i - 1 == len(progresses) - 1:
                answer.append(c)
        else:
            if c > 0:
                answer.append(c)
                c = 0

            d += 1

    return answer
