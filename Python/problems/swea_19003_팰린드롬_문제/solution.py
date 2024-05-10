import sys
import math

sys.stdin = open("input.txt", "r")


def is_pair(x, y):
    if len(x) != len(y):
        return False

    is_valid = True
    for i in range(0, len(x)):
        if x[i] != y[len(y) - i - 1]:
            is_valid = False
            break

    return is_valid


def is_palindrome(word):
    half = math.floor(len(word) / 2)
    head = word[:half]
    tail = word[half:]

    is_valid = True
    for i in range(0, half):
        if head[i] != tail[len(tail) - i - 1]:
            is_valid = False
            break

    return is_valid


def solution():
    TC = int(input())

    for test_case in range(1, TC + 1):
        N, M = map(int, input().split())
        words = [input() for _ in range(0, N)]

        palindrome = []
        pairs = []
        visited = []
        for i in range(0, len(words)):
            if is_palindrome(words[i]):
                palindrome.append(words[i])
                visited.append(words[i])
                continue

            for j in range(i + 1, len(words)):
                if words[i] in visited or words[j] in visited:
                    continue

                if is_pair(words[i], words[j]):
                    pairs.append(words[i])
                    pairs.append(words[j])
                    visited.append(words[i])
                    visited.append(words[j])

        total = 0
        if len(palindrome) > 0:
            total = M
        if len(pairs) > 0:
            count = len(pairs) * M
            if len(palindrome) > 0:
                count += M
            total = max(total, int(count))

        print(f"#{test_case} {total}")
        # print(f"N={N}, M={M}, words={words}, palindrome={palindrome} pairs={pairs}")


solution()
