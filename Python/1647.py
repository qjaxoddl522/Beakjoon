import sys
input = lambda: sys.stdin.readline().rstrip()

def main() -> None:
    N, M = map(int, input().split())
    line = []
    for _ in range(M):
        line.append(list(map(int, input().split())))
    line.sort(key=lambda x: x[2])
    
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
    connected = 0
    root = [i for i in range(N+1)]
    rank = [0] * (N+1)
    for a, b, c in line:
        if connected >= N-2:
            break
        if find(a) != find(b):
            union(a, b)
            connected += 1
            result += c
    print(result)

main()