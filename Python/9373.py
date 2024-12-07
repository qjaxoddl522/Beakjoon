import sys
input = lambda: sys.stdin.readline().rstrip()

def custom_round(n, k):
    n *= 10**k
    if n - int(n) >= 0.5:
        return (int(n) + 1) / 10**k
    else:
        return (int(n)) / 10**k

def main() -> None:
    w = int(input())   # 복도의 너비
    n = int(input())   # 센서의 개수
    line = []
    sensor = []
    for i in range(2, n+2):
        x1, y1, r1 = map(int, input().split())
        # 양쪽 벽도 노드로 취급 (왼쪽0, 오른쪽1)
        line.append((0, i, x1-r1))
        line.append((1, i, (w-x1)-r1))

        # 다른 센서들과 간선 추가
        for j in range(2, len(sensor)+2):
            x2, y2, r2 = sensor[j-2]
            line.append((i, j, ((x2-x1)**2+(y2-y1)**2)**(1/2) - (r1+r2)))
        sensor.append((x1, y1, r1))
    line.sort(key=lambda x: x[2])

    def union(n1, n2):
        r1, r2 = find(n1), find(n2)
        if rank[r1] > rank[r2]:
            root[r2] = r1
        elif rank[r1] < rank[r2]:
            root[r1] = r2
        else:
            if root[r1] < root[r2]:
                root[r2] = r1
                rank[r1] += 1
            else:
                root[r1] = r2
                rank[r2] += 1
    def find(node):
        if root[node] != node:
            root[node] = find(root[node])
        return root[node]
    
    root = [i for i in range(n+3)]
    rank = [0] * (n+3)
    for a, b, c in line:
        if find(a) != find(b):
            union(a, b)
            # 양쪽 벽이 이어지는 순간 간선의 길이가 정답
            if find(0) == find(1):
                print(max(0, custom_round(c/2, 6)))
                break
    # n == 0
    else:
        print(custom_round(w/2, 6))

for _ in range(int(input())):
    main()