import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(int(1e9))

def union(n1, n2):
    r1, r2 = find(n1), find(n2)
    if r1 == r2:
        return
    root[r2] = r1

def find(n):
    if root[n] != n:
        root[n] = find(root[n])
    return root[n]

G = int(input())
P = int(input())
root = [i for i in range(G+1)]
ans = 0

for _ in range(P):
    g = int(input())

    root_g = find(g)
    #자리가 있음
    if root_g > 0:
        #도킹할 때마다 루트를 앞으로 당겨 0이 되면 자리가 없어진다
        union(root_g-1, root_g)
        ans += 1
    #자리가 없으면 종료
    else:
        break
print(ans)
