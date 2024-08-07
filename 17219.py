import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
d = dict()
for _ in range(N):
    site, pswd = input().split()
    d[site] = pswd

for _ in range(M):
    print(d[input()])
