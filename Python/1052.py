N, K = map(int, input().split())

bottle = 0

while bin(N).count('1') > K:
    index = bin(N)[::-1].index('1') #1이 오른쪽에서 몇 번째에 있는지 찾기
    bottle += 2**index #2^(index) 만큼 더하기
    N += 2**index #2^(index) 만큼 더하기
    
print(bottle)
