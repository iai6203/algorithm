# 프로그래머스 - 단어 변환
#
# https://school.programmers.co.kr/learn/courses/30/lessons/43163


import collections


def solution(begin, target, words):
    if target not in words:
        return 0

    def bfs():
        answer = 0
        queue = collections.deque()
        visited = [False for _ in range(len(words))]

        queue.append((begin, 0))

        while len(queue) > 0:
            current_word, current_count = queue.popleft()

            if current_word in words:
                visited[words.index(current_word)] = True

            # print(f"word={current_word}, count={current_count}, visited={visited}")

            if current_word == target:
                answer = current_count
                break

            for i, word in enumerate(words):
                if visited[i] == True:
                    continue

                count = 0
                for position in range(len(current_word)):
                    if current_word[position] != word[position]:
                        count += 1

                    if count > 1:
                        break

                if count == 1:
                    queue.append((word, current_count + 1))

        return answer

    return bfs()
