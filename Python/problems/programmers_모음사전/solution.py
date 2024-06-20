# 프로그래머스 - 모음사전
#
# https://school.programmers.co.kr/learn/courses/30/lessons/84512

from collections import deque


next_chars = {"A": "E", "E": "I", "I": "O", "O": "U", "U": "A"}


def solution(word):
    count = 1
    chars = deque(["A"])

    while word != "".join(chars):
        if len(chars) == 5:
            while chars[-1] == "U":
                chars.pop()

            chars[-1] = next_chars[chars[-1]]
        else:
            chars.append("A")

        count += 1

    return count


print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))
