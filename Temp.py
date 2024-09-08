import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int,input().split()))
highest = [arr[0],arr[1],arr[2]]
lowest = [arr[0],arr[1],arr[2]]
for i in range(0,n - 1):
    arr = list(map(int,input().split()))
    highest[0] += max(arr[0],arr[1])
    highest[1] += max(arr[0],arr[1],arr[2])
    highest[2] += max(arr[1],arr[2])
    lowest[0] += min(arr[0],arr[1])
    lowest[1] += min(arr[0],arr[1],arr[2])
    lowest[2] += min(arr[1],arr[2])
print(max(highest),min(lowest))