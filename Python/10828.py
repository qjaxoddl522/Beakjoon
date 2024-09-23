import sys
input = sys.stdin.readline

stack = []

N = int(input())
for _ in range(N):
    cmd = input().rstrip().split()

    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        print(stack.pop()) if stack else print(-1)
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        print(0) if stack else print(1)
    elif cmd[0] == 'top':
        print(stack[-1]) if stack else print(-1)
