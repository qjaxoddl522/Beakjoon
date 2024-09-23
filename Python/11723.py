import sys
input = sys.stdin.readline

S = 0
for _ in range(int(input().rstrip())):
    # 명령어 할당
    inp = input().rstrip().split()
    cmd = inp[0]
    if len(inp) > 1:
        x = int(inp[1])

    if cmd == 'add':
        S = S | (1 << x) # x번째 1로 만들기
    elif cmd == 'remove':
        S = S & (~(1 << x)) # x번째 0으로 만들기
    elif cmd == 'check':
        print(int(S & (1 << x) != 0)) # x번째 빼고 전부 0 만든 후 x번째가 0인지 확인
    elif cmd == 'toggle':
        S = (S ^ (1 << x)) # x번째를 XOR 연산
    elif cmd == 'all':
        S = (1 << 21) - 1 #1000...을 만들고 -1 하여 1111...
    elif cmd == 'empty':
        S = 0
