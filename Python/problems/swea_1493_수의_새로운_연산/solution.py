import sys

sys.stdin = open("input.txt", "r")


def find_by_number(n):
    global cursor, number_memory

    if number_memory.get(n):
        return number_memory[n]

    while cursor["number"] <= n:
        number_memory[cursor["number"]] = (cursor["row"], cursor["col"])
        position_memory[f"{cursor['row']},{cursor['col']}"] = cursor["number"]

        if cursor["col"] == 1:
            cursor["head"] += 1
            cursor["row"] = 1
            cursor["col"] = cursor["head"]
        else:
            cursor["row"] += 1
            cursor["col"] -= 1

        cursor["number"] += 1

    return number_memory[n]


def find_by_position(row, col):
    if position_memory.get(f"{row},{col}"):
        return position_memory[f"{row},{col}"]

    while not position_memory.get(f"{row},{col}"):
        find_by_number(cursor["number"])

    return position_memory[f"{row},{col}"]


T = int(input())
number_memory = {}
position_memory = {}
cursor = {"number": 1, "head": 1, "row": 1, "col": 1}

for test_case in range(1, T + 1):
    p, q = map(int, input().split())

    p_pos = find_by_number(p)
    q_pos = find_by_number(q)
    t_pos = (p_pos[0] + q_pos[0], p_pos[1] + q_pos[1])

    answer = find_by_position(t_pos[0], t_pos[1])

    print(f"#{test_case} {answer}")
