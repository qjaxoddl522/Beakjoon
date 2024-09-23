import sys
input = sys.stdin.readline

X = int(input())
price = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    price += a * b

print("Yes" if X == price else "No")
