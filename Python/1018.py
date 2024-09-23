n, m = list(map(int,input().split()))
chess = []
for _ in range(n):
    chess.append(input())
numMin = 32
for stx in range(n-7): #(0, 1, 2)
    for sty in range(m-7): #(0, 1, 2, 3, 4, 5)
        for alpha in (['W', 'B'], ['B', 'W']):
            num = 0
            for x in range(stx, stx+8):
                for y in range(sty, sty+8):
                    if alpha[(x+y)%2] != chess[x][y]:
                        num += 1
            numMin = min(numMin, num)
print(numMin)
