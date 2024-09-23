import sys
input = lambda: sys.stdin.readline().rstrip()

A, B, C = int(input()), int(input()), int(input())

print(A+B-C)
print(int(str(A)+str(B))-C)
