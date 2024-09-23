import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    coor = list(map(int, input().split()))
    # 각 좌표를 1, 2, 3으로 나눈 몫
    moc = [[] for _ in range(3)]
    for i in range(3):
        for div in range(1, 4):
            moc[i].append(coor[i] // div)
    print(moc)

for _ in range(int(input())):
    solve()