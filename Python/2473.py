import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    ls = sorted(list(map(int, input().split())))
    
    answer = None
    minHap = float('inf')
    # 가장 왼쪽인 i를 고정시키고 투포인터 반복
    for i in range(N-2):
        s, e = i+1, N-1
        while s < e:
            curSum = ls[s] + ls[e] + ls[i]
            if minHap > abs(curSum):
                minHap = abs(curSum)
                answer = (ls[s], ls[e], ls[i])
            
            if curSum < 0:
                s += 1
            elif curSum > 0:
                e -= 1
            else:
                print(*sorted(answer))
                return
    
    print(*sorted(answer))

main()