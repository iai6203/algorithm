# 프로그래머스 - 다음 큰 숫자
#
# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def is_available(n1, n2):
    if not n1 < n2:
        return

    bn1 = bin(n1).split("0b")[1]
    bn2 = bin(n2).split("0b")[1]
    if list(bn1).count("1") != list(bn2).count("1"):
        return False

    return True


def solution(n):
    answer = 0

    cn = n
    while answer == 0:
        if is_available(n, cn):
            answer = cn
            break

        cn += 1

    return answer
