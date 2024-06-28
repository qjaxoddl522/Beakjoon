import sys
input = lambda : sys.stdin.readline().rstrip()

def find(n):
    if root[n] != n:
        root[n] = find(root[n])
    return root[n]

def union(n1, n2):
    r1 = find(n1)
    r2 = find(n2)

    if r1 == r2:
        return
    
    if rank[r1] > rank[r2]:
        root[r2] = r1
    elif rank[r1] < rank[r2]:
        root[r1] = r2
    else:
        root[r1] = r2
        rank[r2] += 1

p, w = map(int, input().split())
c, v = map(int, input().split())
root = [i for i in range(p)]
rank = [0 for _ in range(p)]
line = []

#간선을 너비 내림차순 정렬
for _ in range(w):
    line.append(list(map(int, input().split())))
line = sorted(line, key=lambda x: x[2], reverse=True)

#정렬된 간선을 연결하며 두 지점이 같은 루트를 가지는 순간
#연결된 것이므로 가장 최근의 간선 너비를 출력
for s, e, width in line:
    union(s, e)
    if find(c) == find(v):
        print(width)
        break
