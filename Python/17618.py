import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    answer = 0
    for n in range(1, N+1):
        hap = 0
        for i in str(n):
            hap += int(i)
        if n%hap == 0:
            answer += 1
    print(answer)

main()