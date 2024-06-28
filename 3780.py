import sys
input = lambda: sys.stdin.readline().rstrip()

def union(n1, n2):
    # 유니온 연산은 부모가 아닌 노드끼리만
    dist[n1] = abs(n2 - n1) % 1000
    root[n1] = n2

def find(n):
    if root[n] != n:
        # 부모를 먼저 찾고 재귀대로 거리를 더해준다
        f = find(root[n])
        dist[n] = (dist[n] + dist[root[n]])
        root[n] = f
    return root[n]

for _ in range(int(input())):
    N = int(input())

    root = [i for i in range(N+1)]
    dist = [0 for i in range(N+1)] # 루트까지의 거리

    while True:
        cmd = input().split()

        if cmd[0] == 'E':
            # 출력 전 거리 갱신
            find(int(cmd[1]))
            print(dist[int(cmd[1])])
        elif cmd[0] == 'I':
            union(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'O':
            break
