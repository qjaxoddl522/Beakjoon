import sys
input = lambda: sys.stdin.readline().rstrip()
import math

# left와 right 사이의 제곱ㄴㄴ수의 갯수
def sieve(left, right):
    cnt = right-left+1
    # 인덱스 0 = left
    nono = [True] * cnt
    for div in range(2, int(right**(1/2))+1):
        square = div ** 2
        # left 이상의 가장 작은 sqaure의 배수
        start = math.ceil(left/square)*square
        for num in range(start, right+1, square): 
            # 이미 제외된 숫자가 아니면 False 설정
            if nono[num-left]:
                nono[num-left] = False
                cnt -= 1
    return cnt

mi, ma = map(int,input().split())
print(sieve(mi, ma))
