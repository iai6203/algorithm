# 프로그래머스 - JadenCase 문자열 만들기
#
# https://school.programmers.co.kr/learn/courses/30/lessons/12951

# 소문자 => 97 ~ 122
# 대문자 => 65 ~ 90

def jaden_case(s):
    ns = ""

    for i in range(len(s)):
        if i == 0:
            if 97 <= ord(s[i]) <= 122:
                ns += s[i].upper()
            else:
                ns += s[i]
        else:
            if 65 <= ord(s[i]) <= 90:
                ns += s[i].lower()
            else:
                ns += s[i]

    return ns


def solution(s):
    answer = ""

    s_l = s.split(" ")

    for i, s_i in enumerate(s_l):
        s_l[i] = jaden_case(s_i)

    answer = " ".join(s_l)

    return answer
