import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import Counter

def solve(A, B, N):
    # 부분합으로 나올 수 있는 경우의 수
    sumA = []
    sumB = []

    for i in range(len(A)):
        curr_sum = 0
        for j in range(i, len(A)):
            curr_sum += A[j]
            sumA.append(curr_sum)
    
    for i in range(len(B)):
        curr_sum = 0
        for j in range(i, len(B)):
            curr_sum += B[j]
            sumB.append(curr_sum)
    
    # sumA의 각 합이 나타나는 횟수를 딕셔너리로
    counterA = Counter(sumA)
    
    # N-sumB[i]가 sumA에 존재하는지 확인
    cnt = 0
    for s in sumB:
        cnt += counterA[N-s]
    
    return cnt

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
print(solve(A, B, T))
