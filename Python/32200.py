import sys
input = lambda: sys.stdin.readline().rstrip()

N, X, Y = map(int, input().split())
subway = list(map(int, input().split()))

daySum = 0
pieceSum = 0
for length in subway:
    day = length // X
    daySum += day
    pieceSum += max(0, length - day * Y)
print(daySum)
print(pieceSum)