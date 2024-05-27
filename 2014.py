import sys
input = sys.stdin.readline
import heapq as hq

K, N = map(int, input().split())
sosu = list(map(int, input().rstrip().split()))

q = []
for i in sosu:
    hq.heappush(q, i)

#N번 수행 후 정답 꺼내기
for i in range(N):
    num = hq.heappop(q)

    #소수 곱해서 추가
    for j in range(K):
        #정수형 범위초과 방지
        if num * sosu[j] < int(1e31):
            hq.heappush(q, num * sosu[j])

        #소수로 나누어 떨어지면 다른 조합의 같은 num 생성을 방지한다
        if num % sosu[j] == 0:
            break

print(num)
