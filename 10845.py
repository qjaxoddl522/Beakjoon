import sys

queue = []
N = int(sys.stdin.readline())
for _ in range(N):
    cmd = sys.stdin.readline().rstrip().split()

    if cmd[0] == 'push':
        queue.insert(0, cmd[1])
    elif cmd[0] == 'pop':
        print(queue.pop()) if len(queue) > 0 else print(-1)
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        print(1) if len(queue) == 0 else print(0)
    elif cmd[0] == 'front':
        print(queue[-1]) if len(queue) > 0 else print(-1)
    elif cmd[0] == 'back':
        print(queue[0]) if len(queue) > 0 else print(-1)
