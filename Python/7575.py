import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
    def search(st):
        fail = [0] * (len(st))
        j = 0
        for i in range(1, len(st)):
            while j > 0 and st[i] != st[j]:
                j = fail[j-1]
            if st[i] == st[j]:
                j += 1
                fail[i] = j
        
        for pr in program:
            find = False
            j = 0
            for i in range(len(pr[0])):
                while j > 0 and pr[0][i] != st[j]:
                    j = fail[j-1]
                if pr[0][i] == st[j]:
                    if j == len(st)-1:
                        find = True
                        break
                    j += 1
            
            if not find:
                for i in range(len(pr[1])):
                    while j > 0 and pr[1][i] != st[j]:
                        j = fail[j-1]
                    if pr[1][i] == st[j]:
                        if j == len(st)-1:
                            find = True
                            break
                        j += 1
            
            if not find:
                return False
        return True
    
    N, K = map(int, input().split())
    program = []
    for _ in range(N):
        input()
        inp = list(map(int, input().split()))
        program.append([inp, inp[::-1]])

    dq = deque()
    for s in program[0][0]:
        dq.append(s)
        if len(dq) == K:
            if search(dq):
                print("YES")
                return
            dq.popleft()
    dq = deque()
    for s in program[0][1]:
        dq.append(s)
        if len(dq) == K:
            if search(dq):
                print("YES")
                return
            dq.popleft()
    print("NO")

main()