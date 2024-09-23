import sys
input = lambda: sys.stdin.readline().rstrip()

def union(n1, n2):
    r1, r2 = find(n1), find(n2)
    if r1 == r2:
        return
    
    if rank[r1] > rank[r2]:
        root[r1] += root[r2]
        root[r2] = r1
    elif rank[r1] < rank[r2]:
        root[r2] += root[r1]
        root[r1] = r2
    else:
        root[r2] += root[r1]
        root[r1] = r2
        rank[r2] += 1

def find(n):
    if root[n] < 0:
        return n
    if root[n] != n:
        root[n] = find(root[n])
    return root[n]

N, M, Q = map(int, input().split())
# 음수면 본인이 루트이며 집합의 크기
root = [-1 for i in range(N+1)]
rank = [0 for _ in range(N+1)]
line = []
for _ in range(M):
    line.append(tuple(map(int, input().split())))

remove_idx = []
for _ in range(Q):
    remove_idx.append(int(input())-1)
# 역순으로 간선을 재생성하기 위해 뒤집음
remove_idx.reverse()

# 제거된 간선 상태
init = [True] * M
for i in remove_idx:
    init[i] = False
for i, node in enumerate(line):
    if init[i]:
        union(node[0], node[1])

# 제거된 간선을 역순으로 유니온하며 비용을 산출
cost = 0
for i in remove_idx:
    n1, n2 = line[i]
    r1, r2 = find(n1), find(n2)
    if r1 != r2:
        cost += abs(root[r1]) * abs(root[r2])
    union(n1, n2)

print(cost)
