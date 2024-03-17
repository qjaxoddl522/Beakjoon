import sys
input = sys.stdin.readline

S = input().rstrip()
N = int(input())
string = [input().rstrip() for _ in range(N)]

dp = [0] * 101 #dp[단어의 길이] = 가능여부
dp[0] = 1

for i in range(len(S)+1):
    for s in string:
        #i가 단어보다 길거나 같고, 직전 단어의 dp == 1이며 s 부분과 같으면 dp = 1
        if i >= len(s) and dp[i-len(s)] == 1 and S[i-len(s):i] == s:
            dp[i] = 1

print(dp[len(S)])
