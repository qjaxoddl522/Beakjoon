import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = [-1] * N

    minn = A[N-1]
    minnIdx = N-1
    for i in range(N-2, -1, -1):
        if A[i] != A[i+1]:
            ans[i] = i + 2
            minn = A[i+1]
            minnIdx = i + 1
        else:
            if A[i] != minn:
                ans[i] = minnIdx + 1

    print(*ans)

main()