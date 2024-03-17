from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
name = [len(input().rstrip()) for _ in range(N)] #이름 길이
ans = 0 #좋은 친구의 수
q = [deque() for _ in range(21)] #이름 길이별 저장할 큐

for i, l in enumerate(name): #i등수 l이름 길이
    while (q[l] and i - q[l][0] > K): #큐가 비어있지 않고 K이상 차이나면 pop
        q[l].popleft()
    if q[l]: #큐 안에 있는 등수의 학생들은 현재 학생과 좋은 친구
        ans += len(q[l])
    q[l].append(i)
print(ans)
