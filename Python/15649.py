import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())

#백트래킹
def bt():
    if len(s) == M:
        print(*s)
        return
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        bt()
        s.pop()
        visited[i] = False

s = [] #스택용 리스트
visited = [False] * (N+1)
bt()
