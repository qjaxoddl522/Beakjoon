import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
    def Spread(r, c):
        sp = current[r][c] // 5
        for nr, nc in ((r, c+1), (r, c-1), (r+1, c), (r-1, c)):
            if 0 <= nr < R and 0 <= nc < C and current[nr][nc] != -1:
                change[nr][nc] += sp
                change[r][c] -= sp

    R, C, T = map(int, input().split())
    current = []
    dust = 0
    upperCleaner = None
    lowerCleaner = None
    for r in range(R):
        temp = deque(map(int, input().split()))
        current.append(temp)
        dust += sum(temp)
        if temp[0] == -1:
            if upperCleaner is None:
                upperCleaner = r
            else:
                lowerCleaner = r
    dust += 2
    
    for _ in range(T):
        # 미세먼지 확산
        change = [[0] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if current[r][c] > 0:
                    Spread(r, c)
        
        for r in range(R):
            for c in range(C):
                current[r][c] += change[r][c]
        
        # 공청기 작동
        current[upperCleaner][0] = 0
        current[lowerCleaner][0] = 0

        temp = None
        start = current[upperCleaner].pop()
        for r in range(upperCleaner-1, -1, -1):
            if r > 0:
                temp = current[r].pop()
            current[r].append(start)
            start = temp
        start = current[lowerCleaner].pop()
        for r in range(lowerCleaner+1, R):
            if r < R-1:
                temp = current[r].pop()
            current[r].append(start)
            start = temp
        
        start = current[0].popleft()
        for r in range(1, upperCleaner):
            temp = current[r].popleft()
            current[r].appendleft(start)
            start = temp
        dust -= start
        start = current[R-1].popleft()
        for r in range(R-2, lowerCleaner, -1):
            temp = current[r].popleft()
            current[r].appendleft(start)
            start = temp
        dust -= start
        current[upperCleaner].appendleft(-1)
        current[lowerCleaner].appendleft(-1)
        
    #print(*current, sep='\n')
    print(dust)

main()