import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main() -> None:
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    inner = [0 for _ in range(N+1)]
    for _ in range(M):
        dir = list(map(int, input().split()))
        for i in range(1, len(dir)-1):
            graph[dir[i]].append(dir[i+1])
            inner[dir[i+1]] += 1
    
    dq = deque()
    for i in range(1, N+1):
        if inner[i] == 0:
            dq.append(i)
    
    result = []
    for _ in range(N):
        if len(dq) == 0:
            print(0)
            return
        
        node = dq.popleft()
        result.append(node)
        for next in graph[node]:
            inner[next] -= 1
            if inner[next] == 0:
                dq.append(next)
    print('\n'.join(map(str, result)))

"""
① 들어오는 간선이 없는(inner가 0인) 정점을 큐에 모두 넣는다.
② 정점 개수만큼 이 행동을 반복한다: 큐의 front 원소를 빼서 그 정점에서 나가는 간선을 모두 삭제한다.
이때 삭제하면서 inner가 0이 된 새로운 정점이 생기면 그것들도 큐에 넣는다.
③ 이때 큐에서 빼는 정점 순서가 위상 정렬 결과다.
"""
main()