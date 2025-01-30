import sys
input = lambda: sys.stdin.readline().rstrip()

def main() -> None:
    N = int(input())
    # x, y, z
    point = [[] for _ in range(3)]
    for i in range(N):
        x, y, z = map(int, input().split())
        point[0].append((x, i))
        point[1].append((y, i))
        point[2].append((z, i))
    for axis in range(3):
        point[axis].sort()
    
    # 인접한 좌표들로 간선 만들기
    line = []
    for axis in range(3):
        for i in range(1, N):
            a, b = point[axis][i], point[axis][i-1]
            line.append((a[1], b[1], a[0] - b[0]))
    line.sort(key = lambda x: x[2])
    
    def union(n1, n2):
        r1, r2 = find(n1), find(n2)
        if rank[r1] > rank[r2]:
            root[r2] = r1
        elif rank[r1] < rank[r2]:
            root[r1] = r2
        else:
            root[r2] = r1
            rank[r1] += 1
    def find(node):
        if root[node] != node:
            root[node] = find(root[node])
        return root[node]
    
    result = 0
    root = [i for i in range(N)]
    rank = [0] * N
    for a, b, c in line:
        if find(a) != find(b):
            union(a, b)
            result += c
    print(result)

main()