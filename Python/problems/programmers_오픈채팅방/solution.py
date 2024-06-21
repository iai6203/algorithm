# 프로그래머스 - 오픈채팅방
#
# https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []

    profiles = {}
    for r in record:
        status = r.split()

        if status[0] == "Enter" or status[0] == "Change":
            profiles[status[1]] = status[2]

    for r in record:
        status = r.split()

        if status[0] == "Enter":
            answer.append(f"{profiles[status[1]]}님이 들어왔습니다.")
        elif status[0] == "Leave":
            answer.append(f"{profiles[status[1]]}님이 나갔습니다.")

    return answer
