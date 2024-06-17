# 순열 (Permutation)

def permutation(n, r):
    ans = []

    def generate(chosen, checklist):
        nonlocal ans

        if len(chosen) == r:
            ans.append(chosen.copy())
            return

        for i in range(len(n)):
            if checklist[i] == 0:
                chosen.append(n[i])
                checklist[i] = 1
                generate(chosen, checklist)
                chosen.pop()
                checklist[i] = 0

    generate([], [0] * len(n))

    return ans
