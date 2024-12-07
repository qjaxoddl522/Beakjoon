import sys
input = lambda: sys.stdin.readline().rstrip()

def main() -> None:
    N = int(input())
    line = []
    star = []
    for i in range(N):
        r, c = map(float, input().split())
        for j in range(len(star)):
            line.append((i, j, ((r-star[j][0])**2 + (c-star[j][1])**2)**(1/2)))
        star.append((r, c))
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