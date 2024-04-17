N, M = map(int, input().split())
ls = []

def dfs(start):
    if len(ls) == M:
        print(*ls)
        return

    for i in range(start, N+1):
        ls.append(i)
        dfs(i)
        ls.pop()

dfs(1)
