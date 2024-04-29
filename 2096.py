import sys
input = sys.stdin.readline

N = int(input())
ls = list(map(int, input().rstrip().split()))

#[각 열의 최소/최대값]
maxdp = ls
mindp = ls

#값을 입력받을 때마다 dp리스트 갱신(슬라이딩 윈도우)
for _ in range(N-1):
    ls = list(map(int, input().rstrip().split()))
    maxdp = [ls[0] + max(maxdp[0], maxdp[1]), ls[1] + max(maxdp), ls[2] + max(maxdp[1], maxdp[2])]
    mindp = [ls[0] + min(mindp[0], mindp[1]), ls[1] + min(mindp), ls[2] + min(mindp[1], mindp[2])]

print(max(maxdp), min(mindp))
