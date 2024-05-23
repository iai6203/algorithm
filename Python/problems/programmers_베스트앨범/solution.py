# 프로그래머스 - 베스트앨범
#
# https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    dict = {}

    for i in range(len(genres)):
        if genres[i] not in dict:
            dict[genres[i]] = {"songs": [], "plays": 0}

        dict[genres[i]]["songs"].append((i, plays[i]))
        dict[genres[i]]["plays"] += plays[i]

    sorted_by_plays = sorted(dict.items(), key=(lambda item: item[1]["plays"]), reverse=True)

    for key, value in sorted_by_plays:
        songs = value["songs"]

        if len(songs) == 0:
            continue
        if len(songs) == 1:
            answer.append(songs[0][0])
            continue

        sorted_songs = sorted(value["songs"], key=(lambda item: item[1]), reverse=True)
        for i in range(2):
            answer.append(sorted_songs[i][0])

    return answer
