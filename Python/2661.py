import sys
input = sys.stdin.readline
sys.setrecursionlimit(99999)

#좋은수열 확인
def check(seq):
    for i in range(1, len(seq)//2+1):
        for j in range(i, len(seq)-i+1):
            if seq[j-i:j] == seq[j:j+i]:
                return False
    return True

def backtrack(seq):
    if len(seq) == N:
        print(seq)
        exit(0)

    for i in ('1', '2', '3'):
        if check(seq+i):
            backtrack(seq+i)

N = int(input().rstrip())
backtrack('')
