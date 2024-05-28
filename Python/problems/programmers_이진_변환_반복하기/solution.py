# 프로그래머스 - 이진 변환 반복하기
#
# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    cout = 0
    cout_rm_zero = 0
    while s != "1":
        x = []

        for c in list(s):
            if c == "0":
                cout_rm_zero += 1
            elif c == "1":
                x.append(c)

        c = len(x)
        s = bin(c).split("0b")[1]

        cout += 1

    return [cout, cout_rm_zero]
