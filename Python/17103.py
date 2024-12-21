import sys
input = lambda: sys.stdin.readline()

def main():
    sosu = [True] * 1000001
    sosu[0] = sosu[1] = False
    for i in range(2, 1001):
        if sosu[i]:
            for j in range(i**2, 1000001, i):
                sosu[j] = False
    sosuList = [i for i in range(1000001) if sosu[i]]

    for _ in range(int(input())):
        N = int(input())
        result = 0
        for s in sosuList:
            if s > N//2:
                break
            if sosu[N-s]:
                result += 1
        print(result)

main()