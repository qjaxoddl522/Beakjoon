import sys

def loop(x, y, n):
    global result
    if x > r or x+n <= r or y > c or y+n <= c: #범위에 맞는지 확인
        result += n**2
        return
    
    if n > 2: #범위에 맞으면 분할정복으로 위치 확인
        n = n//2
        loop(x, y, n)
        loop(x, y+n, n)
        loop(x+n, y, n)
        loop(x+n, y+n, n)
    else:
        if x == r and y == c:
            print(result)
        elif x == r and y+1 == c:
            print(result+1)
        elif x+1 == r and y == c:
            print(result+2)
        else:
            print(result+3)
        sys.exit()
        
N, r, c = map(int,input().split())
result = 0
loop(0, 0, 2**N)

"""
N, r, c = map(int,input().split())
result = -1

def loop(x, y, n): #첫 x좌표, 첫 y좌표, 길이
    global result
    if n != 1: #길이가 최소가 아니면 z순서 4분할 루프
        n = n//2
        loop(x, y, n)
        loop(x+n, y, n)
        loop(x, y+n, n)
        loop(x+n, y+n, n)
    else: #최소일때 직접 계산
        for i in range(y, y+n):
            for j in range(x, x+n):
                result += 1
                if r == i and c == j:
                    return print(result)

loop(0, 0, 2**N)
#시간초과
"""
