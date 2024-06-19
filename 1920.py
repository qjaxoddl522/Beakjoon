import sys
input = sys.stdin.readline

N = int(input())
arr = set(map(int, input().rstrip().split()))
M = int(input())
question = list(map(int, input().rstrip().split()))

for i in question:
    print(1 if i in arr else 0)
