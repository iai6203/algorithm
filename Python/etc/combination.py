# 조합 (Combination)

def combination(n, r):
    ans = []

    def generate(chosen, begin_index):
        nonlocal ans

        if len(chosen) == r:
            ans.append(chosen.copy())
            return

        for i in range(begin_index, len(n)):
            chosen.append(n[i])
            generate(chosen, i + 1)
            chosen.pop()

    generate([], 0)

    return ans
