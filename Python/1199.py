import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    inp = [list(map(int, input().split())) for _ in range(N)]
    graph = [dict() for _ in range(N)]

    for i in range(N):
        lineAmount = 0  # 가능 여부 판단을 위한 간선 수
        for j in range(N):
            lineAmount += inp[i][j]
            if inp[i][j]:
                graph[i][j] = inp[i][j]
        if lineAmount%2 == 1:
            print(-1)
            return

    # 스택으로 구현하여 오버헤드 방지
    def Dfs(start):
        stack = []
        stack.append(start)
        path = []
        while stack:
            node = stack[-1]
            if graph[node]:
                for next, _ in graph[node].items():
                    graph[node][next] -= 1
                    graph[next][node] -= 1
                    if graph[node][next] == 0:
                        del graph[node][next]
                        del graph[next][node]
                    stack.append(next)
                    break  # 다음 dfs를 위함
            else:  # 남은 간선이 없음
                path.append(node+1)
                del stack[-1]
        return path

    print(*Dfs(0))

main()

# 시간초과
"""
def main() -> None:
    # 간선(단방향) 구조체
    class Edge:
        cnt = 0      # 왕복 가능 횟수
        point = None # 가리키고 있는 정점
        other = None # 반대방향 간선
        def __init__(self, cnt, point):
            self.cnt = cnt
            self.point = point
        def __repr__(self):
            return f"{self.cnt}, pointed:{self.point}"

    # 컴포넌트 방문
    def Dfs(node):
        result = 1
        visited[node] = True
        for line in graph[node]:
            if not visited[line.point]:
                result += Dfs(line.point)
        return result
    
    def EulerPath(node):
        for line in graph[node]:
            if line.cnt > 0:
                line.cnt -= 1
                line.other.cnt -= 1
                EulerPath(line.point)
        path.append(node+1)

    N = int(input())
    graph = [[] for _ in range(N)]
    degree = [0] * N
    for i in range(N):
        inp = list(map(int, input().split()))
        for j in range(i):
            if inp[j] > 0:
                e1 = Edge(inp[j], j)
                e2 = Edge(inp[j], i)
                e1.other = e2
                e2.other = e1
                graph[i].append(e1)
                graph[j].append(e2)
                degree[i] += inp[j]
                degree[j] += inp[j]
    
    # 간선이 홀수개인 정점이 있는지 확인
    for i in range(N):
        if degree[i]%2 == 1:
            print(-1)
            return
    
    visited = [False] * N
    compNum = 0
    # 섬에서 시작하는 경우 방지
    start = 0
    for i in range(N):
        if not visited[i]:
            compSize = Dfs(i)
            if compSize > 1:
                start = i
                compNum += 1
            # 간선이 존재하는 컴포넌트가 2개 이상이면 불가능
            if compNum > 1:
                print(-1)
                return
    
    path = []
    EulerPath(start)
    print(*path)

main()
"""