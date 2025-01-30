import sys
input = lambda: sys.stdin.readline().rstrip()

N, B = map(int, input().split())
result = ''
while N > 0:
    N, mod = divmod(N, B)
    result += str(mod) if mod < 10 else chr(ord('A')+mod-10)
print(result[::-1])