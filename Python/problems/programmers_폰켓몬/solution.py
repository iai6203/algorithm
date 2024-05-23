# 프로그래머스 - 폰켓몬
#
# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    category = {}

    for num in nums:
        if category.get(num):
            category[num] += 1
        else:
            category[num] = 0

    category_count = len(category.keys())

    return min(int(len(nums) / 2), category_count)
