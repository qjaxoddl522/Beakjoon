import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

N = int(input())

tree = [[] for _ in range(N+1)] #연결된 트리 구조
node = [[], [0, 0]] #node[i][j] = i번째 섬의 j[(양, 늑대), 마릿수]

for i in range(2, N+1):
    sw, num, connected = input().rstrip().split()
    tree[int(connected)].append(i)
    node.append([sw, int(num)])

def dfs(n):
    result = 0
    for i in tree[n]:
        result += dfs(i)

    if node[n][0] == 'W': #늑대
        result -= node[n][1]
        if result < 0:
            result = 0
    else: #양
        result += node[n][1]
    return result

print(dfs(1))
