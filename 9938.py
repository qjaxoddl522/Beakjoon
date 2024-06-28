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

N, L = map(int, input().split())
root = [i for i in range(L+1)]
surap = [0 for _ in range(L+1)] # 어떤 술병이 들어있는가

for i in range(1, N+1):
    a, b = map(int, input().split())
    root_a, root_b = find(a), find(b)
    if surap[root_a] == 0:
        surap[root_a] = i
        print("LADICA")
    elif surap[root_b] == 0:
        surap[root_b] = i
        print("LADICA")
    else:
        print("SMECE")
    union(b, a) # 부모를 비어있는 쪽으로 유니온
