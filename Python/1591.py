import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N, M = map(int, input().split())
    graph = dict()
    degree = dict()
    for _ in range(N-M+1):
        ls = list(map(int, input().split()))
        a, b = tuple(ls[:-1]), tuple(ls[1:])
        if a not in graph:
            graph[a] = dict()
        if b not in graph[a]:
            graph[a][b] = 0
        if a not in degree:
            degree[a] = 0
        if b not in degree:
            degree[b] = 0
        graph[a][b] += 1
        degree[a] += 1
        degree[b] -= 1

    # 시작점 정하기
    start = None
    for node, deg in degree.items():
        if start == None:
            start = node
        if deg == 1:
            start = node
    
    def Dfs(start):
        stack = [start]
        path = []
        while stack:
            node = stack[-1]
            if node in graph and graph[node]:
                for next, _ in graph[node].items():
                    graph[node][next] -= 1
                    if graph[node][next] == 0:
                        del graph[node][next]
                    stack.append(next)
                    break
            else:
                path.append(node)
                del stack[-1]
        
        # 맨 처음 수열로 시작해서 그 다음 수열부터는 끝부분 하나씩만 이어붙인다
        result = list(path[-1])
        for i in range(len(path)-2, -1, -1):
            result.append(path[i][-1])
        return result
    
    print(*Dfs(start))

main()