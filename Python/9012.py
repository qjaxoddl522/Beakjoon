import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    s = list(input().rstrip())
    
    stack = []
    possible = True
    for i in s:
        if i == '(':
            stack.append('(')
        elif stack:
            stack.pop()
        else:
            possible = False
            break
    if stack:
        possible = False
    print("YES") if possible else print("NO")
