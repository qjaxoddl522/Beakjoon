import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000) #재귀 상한 늘리기

N = int(input())
pic = [[], []]
for _ in range(N):
    s = input().rstrip()
    pic[0].append(list(s))
    s = s.replace('R', 'G') #적록색약 통일
    pic[1].append(list(s))

global color
color = 'X'
ans = [0, 0] #ans[0] = 보통 ans[1] = 적록색약

def dfs(x, y, colorBlind):
    global color
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if pic[colorBlind][x][y] == color:
        pic[colorBlind][x][y] = 'X'
        dfs(x+1, y, colorBlind)
        dfs(x-1, y, colorBlind)
        dfs(x, y+1, colorBlind)
        dfs(x, y-1, colorBlind)
        return True
    return False

for colorBlind in (0, 1):
    for i in range(N):
        for j in range(N):
            if pic[colorBlind][i][j] != 'X':
                color = pic[colorBlind][i][j]
                if dfs(i, j, colorBlind):
                    ans[colorBlind] += 1

print(' '.join(map(str, ans)))
