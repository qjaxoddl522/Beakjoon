import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    H, N = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]
    # 반드시 정렬할 필요는 없으나 속도순 정렬 후 dp[H]를 찾자마자 탈출하면 시간 단축 가능
    info.sort(key= lambda x: -x[1])

    # 키의 합이 i일때 최소속도
    dp = [0] * (H+1)
    dp[0] = float('inf')
    for tall, speed in info:
        for i in range(H, tall-1, -1):
            dp[i] = max(dp[i], min(dp[i-tall], speed))
        if dp[H] != 0:
            break
    print(dp[H])

main()