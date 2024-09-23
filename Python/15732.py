import sys
input = lambda: sys.stdin.readline().rstrip()

N, K, D = map(int, input().split())
rule = []
for _ in range(K):
    rule.append(list(map(int, input().split())))
    
start = 0
end = N
while start <= end:
    mid = (start + end) // 2

    # mid번 상자까지 담긴 도토리의 수
    cnt = 0
    for s, e, sep in rule:
        # mid 이후에 시작되는 규칙은 무시
        if s > mid:
            continue
        if e < mid:
            cnt += (e - s) // sep + 1
        else:
            cnt += (mid - s) // sep + 1

        # 도토리가 너무 많이 담겼으면 mid가 과도하게 큰것
        if cnt >= D:
            end = mid - 1
            ans = mid
            break
    # 정상적으로 모두 담겼으면 mid가 작은 것
    else:
        start = mid + 1

print(ans)
