# 프로그래머스 - 2개 이하로 다른 비트
#
# https://school.programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    ans = [0] * len(numbers)

    for i, number in enumerate(numbers):
        if number % 2 == 0:
            ans[i] = number + 1
        else:
            bin_number = "0" + bin(number)[2:]

            zero_index = bin_number.rindex("0")

            bin_number_list = list(bin_number)
            bin_number_list[zero_index] = "1"
            bin_number_list[zero_index + 1] = "0"

            ans[i] = int("".join(bin_number_list), 2)

    return ans


print(solution([2, 7]))  # [3, 11]
