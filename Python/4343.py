import sys
input = lambda: sys.stdin.readline().rstrip()

def main() -> None:
    for _ in range(int(input())):
        S, P = map(int, input().split())
        line = []
        point = []
        for i in range(P):
            r, c = map(float, input().split())
            for j in range(len(point)):
                line.append((i, j, ((r-point[j][0])**2 + (c-point[j][1])**2)**(1/2)))
            point.append((r, c))
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
        
        connectLine = []
        root = [i for i in range(P)]
        rank = [0] * P
        for a, b, c in line:
            if find(a) != find(b):
                union(a, b)
                connectLine.append(c)
        
        print('%.2f'%connectLine[-S] if S <= len(connectLine) else '%.2f'%0)

main()