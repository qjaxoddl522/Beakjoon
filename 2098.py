import sys
input = sys.stdin.readline

N = int(input().rstrip())
mapp = [list(map(int, input().rstrip().split())) for _ in range(N)]
dp = {} #(현재 위치, 방문한 노드) = 비용

def dfs(n, visited): #현재 위치, 방문한 노드(비트마스킹)
    if visited == (1 << N) - 1: #(모든 숫자가 1이므로)모든 노드를 방문한 경우
        if mapp[n][0] != 0: #다시 시작점으로 갈 수 있으면 비용 반환
            return mapp[n][0]
        else:
            return int(1e9) #갈 수 없으면 최대값 반환

    if (n, visited) in dp: #이미 방문했으면 값 가져오기
        return dp[(n, visited)]

    cost = int(1e9)
    for i in range(1, N):
        if mapp[n][i] == 0 or (visited & (1 << i)): #갈수 없거나 이미 방문함
            continue
        cost = min(dfs(i, visited | (1 << i)) + mapp[n][i], cost) #다음 노드 방문
    
    dp[(n, visited)] = cost #구한 최소 비용 담기
    return cost

print(dfs(0, 1))
