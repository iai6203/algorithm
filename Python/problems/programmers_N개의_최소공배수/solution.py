# 프로그래머스 - N개의 최소공배수
#
# https://school.programmers.co.kr/learn/courses/30/lessons/12953

def solution(arr):
    numbers = arr.copy()

    m = max(numbers)
    while True:
        if numbers.count(m) == len(arr):
            return m

        for i, n in enumerate(numbers):
            if n < m:
                numbers[i] += arr[i]

        m = max(numbers)
