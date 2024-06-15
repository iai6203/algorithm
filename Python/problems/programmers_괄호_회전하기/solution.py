# 프로그래머스 - 괄호 회전하기
#
# https://school.programmers.co.kr/learn/courses/30/lessons/76502

from collections import deque


def check(s):
    s_q = deque(list(s))
    check_q = deque()

    while s_q:
        char = s_q.popleft()

        # 괄호를 시작한다면 큐에 추가
        if char == "(" or char == "{" or char == "[":
            check_q.append(char)
            continue

        # 괄호를 닫는다면 짝을 확인
        if char == ")" or char == "}" or char == "]":
            # `check_q`가 비어있다면 확인할 짝조차 없다는 뜻
            if len(check_q) == 0:
                return False

            if check_q[-1] == "(" and char == ")":
                check_q.pop()
                continue
            if check_q[-1] == "{" and char == "}":
                check_q.pop()
                continue
            if check_q[-1] == "[" and char == "]":
                check_q.pop()
                continue

    # 정리되지 않은 괄호가 있을 경우 실패
    if len(check_q) > 0:
        return False

    return True


def solution(s):
    ans = 0

    s_q = deque(list(s))
    for _ in range(len(s)):
        check_s = "".join(s_q)

        if check(check_s):
            ans += 1

        s_q.append(s_q.popleft())

    return ans

