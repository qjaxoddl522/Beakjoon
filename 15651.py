import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
ls = []

def backtracking():
    #길이 만족
    if len(ls) == M:
        print(' '.join(ls))
        return
    
    for i in range(1, N+1):
        ls.append(str(i))
        backtracking()
        ls.pop()

backtracking()
