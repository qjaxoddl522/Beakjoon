import sys
input = sys.stdin.readline

a,b = map(int, input().split())
for i in range(a, a*b+1, a):
    if i%b==0:
        print(i)
        break
