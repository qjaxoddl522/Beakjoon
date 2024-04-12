import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
ls = []

def dfs(start):
    #길이가 충족되면 탈출
    if len(ls) == M:
        print(*ls)
        return

    for i in range(start, N+1):
        if i not in ls:
            #중복이 아니면 리스트 추가하고 dfs실행 후 되돌려 백트래킹
            ls.append(i)
            dfs(i+1)
            ls.pop()
dfs(1)
