import sys
n = int(sys.stdin.readline())
nNum = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
mNum = list(map(int, sys.stdin.readline().split()))

nDic = dict(zip(nNum, range(n)))

for i in range(m):
    print(0 if mNum[i] not in nDic else 1, end=" ")
