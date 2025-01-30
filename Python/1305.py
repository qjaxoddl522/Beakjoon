import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    S = input()
    
    fail = [0] * len(S)
    j = 0
    for i in range(1, len(S)):
        while j > 0 and S[i] != S[j]:
            j = fail[j-1]
        if S[i] == S[j]:
            j += 1
            fail[i] = j
    
    # 문자열의 길에서 최대 반복 구간 길이만큼을 뺀 값이 가장 짧은 문자열의 길이
    print(N-fail[N-1])

main()