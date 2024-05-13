import sys
input = sys.stdin.readline

N, W = map(int, input().split())
line = [0 for _ in range(N+1)] #간선의 수
for _ in range(N-1):
    U, V = map(int, input().split())
    line[U] += 1
    line[V] += 1

#끝난 결과 물의 기댓값 0 초과인 정점은 리프노드밖에 남지 않으므로,
#답은 (처음 1번 노드에 고인 물의 양)/(리프 노드의 수)가 된다.

leafNum = 0
for i in range(2, N+1): #루트 노드 제외
    if line[i] == 1: #연결된 정점이 하나면 리프노드
        leafNum += 1
print(W/leafNum)
