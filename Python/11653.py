import sys
# 이게 더 시간이 오래걸림
print = lambda x: sys.stdout.write(str(x)+'\n')

N = int(input())
i = 2
while i**2 <= N:
    while N%i == 0:
        N //= i
        print(i)
    i += 1
if N != 1:
    print(N)
