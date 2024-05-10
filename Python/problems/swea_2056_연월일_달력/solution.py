import sys

sys.stdin = open("input.txt", "r")

max_day = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}


def solution():
    T = int(input())

    for test_case in range(1, T + 1):
        string = input()
        year = string[0:4]
        month = string[4:6]
        day = string[6:8]

        # 년도 검사
        # if len(str(int(year))) != 4:
            # print(f"invalid year ({year})")
            # print(f"#{test_case} -1")
            # continue

        # 월 검사
        if not 1 <= int(month) <= 12:
            # print(f"invalid month ({month})")
            print(f"#{test_case} -1")
            continue

        # 일자 검사
        if int(day) > max_day[int(month)]:
            # print(f"invalid day ({day})")
            print(f"#{test_case} -1")
            continue

        print(f"#{test_case} {year}/{month}/{day}")


solution()
