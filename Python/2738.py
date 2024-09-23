import sys
n, m = map(int, sys.stdin.readline().split())
a, b = [], []
for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))
for _ in range(n):
    b.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    temp = []    
    for j in range(m):
        temp.append(a[i][j]+b[i][j])
    print(' '.join(map(str, temp)))
"""
입력
3 3
1 1 1
2 2 2
0 1 0
3 3 3
4 4 4
5 5 100

출력
4 4 4
6 6 6
5 6 100
"""
