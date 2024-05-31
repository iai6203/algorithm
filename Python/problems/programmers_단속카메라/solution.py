# 프로그래머스
#
# https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 0

    c_routes = routes.copy()
    c_routes.sort(key=(lambda item: item[1]))

    camera = c_routes[0][1]
    answer += 1

    for i in range(1, len(c_routes)):
        route = c_routes[i]

        if route[0] > camera:
            camera = route[1]
            answer += 1

    return answer
