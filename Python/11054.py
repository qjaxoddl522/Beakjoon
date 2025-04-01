import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    L = list(map(int, input().split()))
    
    dpInc = [1] * N
    dpDec = [1] * N
    for i in range(1, N):
        for j in range(i):
            if L[i] > L[j]:
                dpInc[i] = max(dpInc[i], dpInc[j] + 1)
            if L[N-i-1] > L[N-j-1]:
                dpDec[N-i-1] = max(dpDec[N-i-1], dpDec[N-j-1] + 1)
    
    result = 0
    # 기준점
    for i in range(N):
        result = max(result, dpInc[i] + dpDec[i])
    print(result - 1)
    
main()