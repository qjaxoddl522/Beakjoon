import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    hap = [list(map(int, input().split())) for _ in range(N)]

    if N == 2:
        print(1, 1)
        return
    
    answer = [0] * N
    # ((a+b) + (a+c) - (b+c)) / 2 = a
    answer[0] = (hap[0][1] + hap[0][2] - hap[1][2]) // 2
    for i in range(1, N):
        answer[i] = hap[0][i] - answer[0]
    print(*answer)
    
main()