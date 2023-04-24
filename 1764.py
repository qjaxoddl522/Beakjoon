import sys
input = sys.stdin.readline

n, m = map(int, input().split())

hear = {}
see = {}
for _ in range(n):
    hear[input().rstrip()] = 0
for _ in range(m):
    see[input().rstrip()] = 0

lst = []
for i in hear:
    if i in see:
        lst.append(i)
lst.sort()
print(len(lst))
for i in lst:
    print(i)
