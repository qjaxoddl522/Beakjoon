tri = []
n, s = 0, 0
while(n < 1000): #삼각수 리스트 생성
    s += 1
    n += s
    tri.append(n)

T = int(input()) #테스트케이스
for _ in range(T):
    k = int(input())
    possible = 0
    for i in tri:
        for j in tri:
            for l in tri:
                if i+j+l == k:
                    possible = 1
                    break
            if possible:
                break
        if possible:
            break
    print(possible)
