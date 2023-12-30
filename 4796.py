c = 0
while True:
    c += 1
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V ==0:
        break
    a = V//P*L #최대일수
    b = V%P #나머지
    if L < b:
        b = L
    print("Case "+str(c)+": "+str(a+b))
