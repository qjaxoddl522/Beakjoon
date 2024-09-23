import sys
input = lambda: sys.stdin.readline().rstrip()

def sieve(n):
    s = set(range(2, n+1))
    for i in range(2, int(n**(1/2))):
        if i in s:
            for j in range(i*i, n+1, i):
                s.discard(j)
    return s

sosu_set = sieve(1000000)
sosu_list = list(sosu_set)
N = int(input())
nums = list(map(int, input().split()))

# nums의 수들을 소인수분해
# {소수: n번째 숫자가 가진 소수의 개수 리스트}
soinsu = dict()
for idx in range(N):
    num = nums[idx]
    while num != 1:
        for sosu in sosu_list:
            if num % sosu == 0:
                if sosu not in soinsu:
                    soinsu[sosu] = [0] * N
                soinsu[sosu][idx] += 1
                num //= sosu
                break

best = 1 # 얻을 수 있는 최대공약수
cnt = 0 # 필요한 횟수

for sosu, ls in soinsu.items():
    sosuCnt = sum(ls) // N # 정상화될 소수들의 개수
    if sosuCnt > 0: # 최대공약수의 일원이 됨
        best *= (sosu ** sosuCnt)
    for n in ls:
        if n < sosuCnt:
            # 정상화를 위해 필요한 수만큼 횟수에 추가
            cnt += (sosuCnt - n)

print(best, cnt)
