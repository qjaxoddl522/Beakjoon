N, K = map(int, input().split())
order = list(map(int, input().split()))
hole = []
result = 0

for i in range(K):
    if order[i] in hole:
        continue
    
    if len(hole) < N:
        hole.append(order[i])
        continue

    idx = 0 #가장 늦게 사용하는 기기 인덱스
    h = 0 #바꿀 플러그
    for plug in hole: #가장 늦게 사용할 기기 찾기
        if plug not in order[i:]:
            h = plug
            break
        elif order.index(plug, i, K) > idx:
            idx = order.index(plug, i, K)
            h = plug
    hole[hole.index(h)] = order[i] #플러그 교체
    result += 1

print(result)
