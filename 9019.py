from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while q:
        n = q.popleft()
        if n == G:
            return visited[n]
        
        D = n * 2 % 10000
        S = (n - 1) % 10000
        #띄어쓰기된 +를 기준으로 떼어지는 자릿수
        L = (n//1000) + (n%1000)*10
        R = (n//10) + (n%10)*1000
        for string, nn in (('D', D), ('S', S), ('L', L), ('R', R)):
            if not visited[nn] and (n != nn):
                visited[nn] = visited[n] + string
                q.append(nn)

for _ in range(int(input())):
    S, G = map(int, input().rstrip().split())

    q = deque()
    q.append(S)
    visited = [None] * 10000
    visited[S] = ''

    print(bfs())
