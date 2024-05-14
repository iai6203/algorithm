import sys
import copy


sys.stdin = open("input.txt", "r")


def get_total_score(scores):
    return (scores[0] * 0.35) + (scores[1] * 0.45) + (scores[2] * 0.2)


def solution():
    T = int(input())

    grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

    for test_case in range(1, T + 1):
        N, K = map(int, input().split())
        per_grade_student_count = int(N / 10)
        students = []
        for i in range(0, N):
            scores = list(map(int, input().split()))
            students.append({
                "key": i,
                "score": get_total_score(scores)
            })
        sorted_students = sorted(
            copy.deepcopy(students),
            key=(lambda x: x["score"]),
            reverse=True
        )

        answer = None
        current_grade_index = 0
        current_grade_count = 0
        for student in sorted_students:
            student["grade"] = grades[current_grade_index]
            current_grade_count += 1

            if K - 1 == student["key"]:
                answer = student["grade"]
                break

            if current_grade_count == per_grade_student_count:
                current_grade_index += 1
                current_grade_count = 0

        print(f"#{test_case} {answer}")


solution()
