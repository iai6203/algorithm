# 프로그래머스 - 여행경로
#
# https://school.programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):
    ans = []
    path = dict()
    use = [0] * len(tickets)

    for i, ticket in enumerate(tickets):
        if ticket[0] not in path:
            path[ticket[0]] = []
        if ticket[1] not in path:
            path[ticket[1]] = []
        path[ticket[0]].append((i, ticket[1]))

    def dfs(current, steps):
        if use.count(0) == 0:
            ans.append(steps.copy())
            return

        for ticket_index, airport in path[current]:
            if use[ticket_index] == 0:
                use[ticket_index] = 1
                steps.append(airport)
                dfs(airport, steps)
                use[ticket_index] = 0
                steps.pop()

    dfs("ICN", ["ICN"])

    ans.sort()

    return ans[0]


# ["ICN", "JFK", "HND", "IAD"]
print(
    solution([
        ["ICN", "JFK"],
        ["HND", "IAD"],
        ["JFK", "HND"],
    ])
)
# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
print(
    solution([
        ["ICN", "SFO"],
        ["ICN", "ATL"],
        ["SFO", "ATL"],
        ["ATL", "ICN"],
        ["ATL", "SFO"],
    ])
)
