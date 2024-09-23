N, K = map(int, input().split())
coin = []
for _ in range(N):
    i = int(input())
    if i <= K: #금액보다 큰 단위는 넣지 않음
        coin.append(i)

result = 0
for i in coin[::-1]: #큰 단위부터
    result += K//i
    K = K%i
print(result)
