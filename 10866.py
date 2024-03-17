from collections import deque
import sys
N = int(sys.stdin.readline())
deq = deque()

for _ in range(N):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == 'push_front':
        deq.appendleft(int(cmd[1]))
    elif cmd[0] == 'push_back':
        deq.append(int(cmd[1]))
    elif cmd[0] == 'pop_front':
        print(deq.popleft()) if deq else print(-1)
    elif cmd[0] == 'pop_back':
        print(deq.pop()) if deq else print(-1)
    elif cmd[0] == 'size':
        print(len(deq))
    elif cmd[0] == 'empty':
        print(0) if deq else print(1)
    elif cmd[0] == 'front':
        print(deq[0]) if deq else print(-1)
    elif cmd[0] == 'back':
        print(deq[-1]) if deq else print(-1)
