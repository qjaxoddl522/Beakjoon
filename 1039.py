from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    ans = -1
    while q:
        n, k = q.popleft()

        if k == K: #횟수 도달
            ans = max(ans, n)
            continue
            
        n = list(str(n))
        for i in range(len(n)-1):
            for j in range(i+1, len(n)):
                if not (i == 0 and n[j] == '0'): #바꿀 가장 앞자리수가 0이 아니면
                    n[i], n[j] = n[j], n[i]
                    nn = int(''.join(n))
                    if (nn, k+1) not in visited:
                        q.append((nn, k+1))
                        visited.add((nn, k+1))
                    n[i], n[j] = n[j], n[i]
    return ans

N, K = map(int, input().rstrip().split())

q = deque()
q.append((N, 0)) #숫자, 교환횟수
visited = set()
visited.add((N, 0))

print(bfs())
