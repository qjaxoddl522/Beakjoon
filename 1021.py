N, M = map(int, input().split())
num = [i+1 for i in range(N)]
aim = list(map(int, input().split()))

def left(ls):
    temp = ls[0]
    for i in range(1, len(ls)):
        ls[i-1] = ls[i]
    ls[-1] = temp
    return ls

def right(ls):
    temp = ls[-1]
    for i in range(len(ls)-1, 0, -1):
        ls[i] = ls[i-1]
    ls[0] = temp
    return ls

ans = 0
while(len(aim) > 0):
    a = aim.pop(0)
    if len(num) / 2 >= num.index(a):
        while(num.index(a) != 0):
            left(num)
            ans += 1
    else:
        while(num.index(a) != 0):
            right(num)
            ans += 1
    num.pop(0)
print(ans)
