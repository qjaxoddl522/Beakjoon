import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
print(N if N != 2 else 3)