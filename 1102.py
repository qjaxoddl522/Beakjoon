import sys
input = sys.stdin.readline

N = int(input().rstrip())
cost = [list(map(int, input().rstrip().split())) for _ in range(N)]
status = input().rstrip()
P = int(input().rstrip())

def dfs(mask, cnt): #(현재 구동 중인 발전소 bitmask, 구동 중인 발전소 개수)
    global dp

    #조건만큼 채웠으면 0 반환하고 끝내기
    if cnt >= P:
        return 0

    #이미 비용을 구했으면 dp 반환
    if dp[mask] != int(1e9):
        return dp[mask]

    for i in range(N):
        #i번째 발전소가 구동중이면
        if mask & (1 << i) != 0:
             for j in range(N):
                 #j번째 발전소(i번째 발전소를 이용해 구동할 발전소)가 구동중이 아니면
                 if mask & (1 << j) == 0:
                     #발전소를 구동한 dp 추가
                     dp[mask] = min(dp[mask], cost[i][j] + dfs(mask | (1 << j), cnt+1))
    return dp[mask]

status_rev = status[::-1] #발전소의 고장 여부를 뒤집어 비트연산을 용이하게
bit, count = 0, 0

for i in status_rev:
    bit = bit << 1
    if i == 'Y': #발전소가 켜져있으면 1
        bit = bit | 1
        count += 1

dp = [int(1e9)] * (1 << N) #dp[현재 구동 중인 발전소 bitmask] = 총 비용

ans = dfs(bit, count)
print(-1 if ans == int(1e9) else ans) #여전히 무한대면 불가능한 경우
