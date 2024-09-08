import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
array = list(map(int, input().split()))

result = 0
value = 0
s = 0

for e in range(N):
    value += array[e]
    
    while value > M:
        value -= array[s]
        s += 1
        
    if value == M:
        result += 1
        
print(result)
