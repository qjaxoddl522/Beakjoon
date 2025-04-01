import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    info = [tuple(map(int, input().split())) for _ in range(N)]
    info.sort()

    total = 0
    for i in range(N):
        total += info[i][1]
    
    nowTotal = 0
    for x, amount in info:
        nowTotal += amount
        if nowTotal >= total / 2:
            print(x)
            break

main()