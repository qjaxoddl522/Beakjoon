import sys
input = lambda : sys.stdin.readline().rstrip()
from itertools import permutations
cases = list(permutations(['1','2','3','4','5','6','7','8','9'], 3))

for _ in range(int(input())):
    t, s, b = map(int, list(input().split()))
    t = list(str(t))
    rmcnt = 0
    for i in range(len(cases)):
        ns = nb = 0
        i -= rmcnt
        for j in range(3):
            if cases[i][j] == t[j]:
                ns += 1
            elif t[j] in cases[i]:
                nb += 1

        if ns != s or nb != b:
            cases.remove(cases[i])
            rmcnt += 1

print(len(cases))
