import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    while True:
        inp = input()
        if inp == "0":
            break

        N, S, T = map(int, inp.split())
        board = [0]
        while len(board)-1 < N:
            board.extend(map(int, input().split()))
        board.append(0)

        # i+j번째 칸에 t턴 만에 도착했을 때 얻는 돈의 최대
        dp = [[-float('inf')] * (T+1) for _ in range(N+2)]
        dp[0][0] = 0

        for t in range(1, T+1):
            for i in range(t-1, N+1):
                for j in range(1, min(S+1, N+2-i)):
                    dp[i+j][t] = max(dp[i+j][t], dp[i][t-1] + board[i+j])
        #print(*dp, sep='\n')
        print(max(dp[N+1]))

main()