# BAEKJOON 2839
#
# 링크 : https://www.acmicpc.net/problem/10814
#
# - 퀵 정렬 방법은 시간 초과!!

cases = int(input())
items = []

for i in range(cases):
    items.append(input())


def extract(item):
    [age, name] = item.split(" ")

    return {"name": name, "age": int(age)}


def split(data):
    medium = int(len(data) / 2)

    left = data[:medium]
    right = data[medium:]

    return [left, right]


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        left_value = extract(left[left_index])
        right_value = extract(right[right_index])

        if left_value["age"] < right_value["age"]:
            result.append(left[left_index])
            left_index += 1
        elif left_value["age"] == right_value["age"]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result


def solution(data):
    if len(data) <= 1:
        return data

    [left, right] = split(data)

    return merge(solution(left), solution(right))


sorted_data = solution(items)
print("\n".join(sorted_data))
