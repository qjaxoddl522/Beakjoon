import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(int(1e9))

def palindrome(l, r):
    if l >= r:
        return 1

    # 양 끝 값이 같으면 안쪽도 팰린드롬인지 확인
    if dp[l][r] == None:
        if ls[l] == ls[r]:
            dp[l][r] = palindrome(l+1, r-1)
        else:
            dp[l][r] = 0

    return dp[l][r]

N = int(input())
ls = list(map(int, input().split()))

# dp[i][j] = i와 j사이가 팰린드롬인지
dp = [[None for _ in range(N)] for _ in range(N)]

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(palindrome(S-1, E-1))
