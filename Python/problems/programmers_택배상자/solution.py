# 프로그래머스 - 택배상자
#
# https://school.programmers.co.kr/learn/courses/30/lessons/131704

from collections import deque


def solution(order):
    ans = 0
    main_belt = deque([i + 1 for i in range(len(order))])
    sub_belt = deque()
    order_cursor = 0

    while main_belt or sub_belt:
        # 메인 벨트의 첫번째 상자가 실어야 할 상자보다 수가 작다면 보조 벨트로 옮긴다.
        if main_belt and main_belt[0] < order[order_cursor]:
            sub_belt.append(main_belt.popleft())
            continue

        # 메인 벨트의 첫번째 상자가 실어야 할 상자라면 싣는다.
        if main_belt and main_belt[0] == order[order_cursor]:
            main_belt.popleft()
            ans += 1
            order_cursor += 1
            continue

        # 보조 벨트의 마지막 상자가 실어야 할 상자라면 싣는다.
        if sub_belt[-1] == order[order_cursor]:
            sub_belt.pop()
            ans += 1
            order_cursor += 1
            continue

        break

    return ans


print(solution([4, 3, 1, 2, 5]))  # 2
print(solution([5, 4, 3, 2, 1]))  # 5
