# 프로그래머스 - 전력망을 둘로 나누기
#
# https://school.programmers.co.kr/learn/courses/30/lessons/86971


def solution(n, wires):
    ans = float("inf")

    # 그래프 구조화
    graph = {}
    for n1, n2 in wires:
        if n1 not in graph:
            graph[n1] = []
        if n2 not in graph:
            graph[n2] = []

        graph[n1].append(n2)
        graph[n2].append(n1)

    # 모든 전력망을 한 개씩 끊어가며 탐색
    for cut_index in range(len(wires)):
        checklist = [0] * (n + 1)
        cut_n1, cut_n2 = wires[cut_index]

        checklist[0] = 1

        count = 0
        stack = [1]

        while stack:
            n1 = stack.pop()

            checklist[n1] = 1
            count += 1

            for n2 in graph[n1]:
                # 잘려있는지 확인
                if (n1 == cut_n1 and n2 == cut_n2) or (n1 == cut_n2 and n2 == cut_n1):
                    continue

                # 방문했는지 확인
                if checklist[n2] == 1:
                    continue

                stack.append(n2)

        ans = min(ans, abs(len(checklist) - 1 - (checklist.count(0) * 2)))

    return ans


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))
