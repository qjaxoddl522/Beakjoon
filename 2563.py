import sys
paper = [[0]*101 for i in range(101)]
for _ in range(int(sys.stdin.readline())):
    coor = list(map(int, sys.stdin.readline().split()))
    for i in range(coor[0], coor[0]+10):
        paper[i][coor[1]:coor[1]+10] = [1]*10
area = 0
for p in paper:
    area += p.count(1)
print(area)

"""
입력
3
3 7
15 7
5 2

출력
260
"""
