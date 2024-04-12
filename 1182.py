import sys
sys.setrecursionlimit(99999)
input = sys.stdin.readline

def dfs(index, summ):
    global ans

    if index == N: #리스트 끝
        return
    
    summ += arr[index]

    if summ == S:
        ans += 1

    #현재 리스트의 인덱스를 더함
    dfs(index+1, summ)
    #현재 리스트의 인덱스를 더하지 않음
    dfs(index+1, summ-arr[index])

N, S = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

ans = 0
dfs(0, 0)
print(ans)
