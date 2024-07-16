import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
vertex = []

for _ in range(N):
    vertex.append(list(map(int,input().split())))
vertex.append(vertex[0])

ans = 0
for i in range(N):
    ans += vertex[i][0] * vertex[i+1][1] -\
           vertex[i+1][0] * vertex[i][1]

print(abs(ans)/2)
