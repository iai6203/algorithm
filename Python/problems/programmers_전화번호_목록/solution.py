# 프로그래머스 - 전화번호 목록
#
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    phone_book.sort()

    for t1, t2 in zip(phone_book, phone_book[1:]):
        if t2.startswith(t1):
            return False

    return True
