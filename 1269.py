import sys
input = sys.stdin.readline

anum, bnum = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
bdic = {b[i] : i for i in range(len(b))}

result = len(set(a+b))
for i in a:
    if i in bdic:
        result -= 1
print(result)
