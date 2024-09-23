import sys
input = sys.stdin.readline

string = [' ' + input().rstrip() for _ in range(2)]
#dp[i][j] = 문자열1 i자리, 문자열2 j자리까지의 최장 공통 부분 수열
dp = [[0] * len(string[1]) for _ in range(len(string[0]))]

for i in range(1, len(string[0])):
    for j in range(1, len(string[1])):
        if string[0][i] == string[1][j]:
            #같으면 이전 LCS 길이에서 더하기
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            #다르면 이전 값들 중 더 긴거 가져오기
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
