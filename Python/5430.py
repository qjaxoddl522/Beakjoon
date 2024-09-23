import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
deq = deque()
for _ in range(T):
    p = input().rstrip() #수행할 함수
    n = int(input()) #배열의 길이
    deq = deque(input().rstrip()[1:-1].split(','))

    if len(deq) == 1 and deq[0] == '': #deque([''])로 저장되는 상황 방지
        deq.pop()
    
    rev = False #뒤집혔는지 확인하는 변수
    for c in p:
        if c == 'R':
            rev = False if rev else True
        elif c == 'D':
            if deq:
                deq.pop() if rev else deq.popleft()
            else:
                print('error')
                break
    else: #에러 없을 경우에만 실행
        if rev:
            deq.reverse()
        print('[{0}]'.format(','.join(deq)))
