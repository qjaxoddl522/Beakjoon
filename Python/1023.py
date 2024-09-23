import sys
input = lambda: sys.stdin.readline().rstrip()

MAX_N = 51
INF = float('INF')

def dpFill(pos, opened, wrong):
    # 끝까지 도달했을 때 중간에 잘못됐거나 열린괄호 수가 더 많을 경우
    # 괄호ㄴㄴ문자열이므로 1 반환
    if pos == N:
        return 1 if wrong or opened != 0 else 0
    if dp[pos][opened + N][wrong] != INF:
        return dp[pos][opened + N][wrong]

    dp[pos][opened+N][wrong] = 0
    # '('를 입력한 경우
    dp[pos][opened+N][wrong] += dpFill(pos+1, opened+1, wrong)
    # ')'를 입력한 경우
    # ')'가 더 많아진 순간 괄호ㄴㄴ문자열
    dp[pos][opened+N][wrong] += dpFill(pos+1, opened-1, wrong\
                                       or opened <= 0)
    return dp[pos][opened+N][wrong]

def tracking(pos, opened, wrong, k):
    if pos == N:
        return
    if dp[pos+1][opened+1+N][wrong] >= k:
        if pos == N-1 and k == 2:
            print(')', end='')
        else:
            print('(', end='')
        tracking(pos+1, opened+1, wrong, k)
    else:
        print(')', end='')
        newk = k - dp[pos+1][opened+1+N][wrong]
        tracking(pos+1, opened-1, wrong or opened <= 0, newk)

N, K = map(int, input().split())

# dp[i번째 문자열][열린괄호 수 - 닫힌괄호 수][이미 괄호ㄴㄴ문자열]
# = 괄호ㄴㄴ문자열의 수
dp = [[[INF, INF] for _ in range(MAX_N * 2)] for _ in range(MAX_N)]

dpFill(0, 0, 0)

if K+1 > dp[0][N][0]:
    print(-1)
else:
    tracking(0, 0, 0, K+1)
