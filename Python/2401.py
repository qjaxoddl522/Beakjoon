import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    L = input()
    N = int(input())

    patterns = []
    fails = []
    
    # 짧은 문자열에 대한 실패함수 만들어놓기
    for _ in range(N):
        s = input()
        fail = [0] * len(s)
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = fail[j-1]
            if s[i] == s[j]:
                j += 1
            fail[i] = j
        
        patterns.append(s)
        fails.append(fail)
    
    dp = [0] * (len(L)+1)
    match = [0] * N

    # 검색하면서 dp 갱신
    for i in range(len(L)):
        dp[i+1] = max(dp[i+1], dp[i])

        for idx in range(N):
            while match[idx] > 0 and L[i] != patterns[idx][match[idx]]:
                match[idx] = fails[idx][match[idx]-1]
            
            if L[i] == patterns[idx][match[idx]]:
                match[idx] += 1
            
            if match[idx] == len(patterns[idx]):
                dp[i+1] = max(dp[i+1], dp[i+1-len(patterns[idx])] + len(patterns[idx]))
                match[idx] = fails[idx][match[idx]-1]
    
    print(dp[len(L)])

main()