N = int(input())
K = int(input())
C = sorted(list(map(int, input().split())))

if K >= N: #센서보다 집중국이 많으면 0
    print(0)
else:
    dis = []
    for i in range(1, N):
        dis.append(C[i]-C[i-1])
    dis.sort(reverse = True) #거리를 내림차순 정렬

    for _ in range(K-1):
        dis.pop(0) #거리가 먼 순서대로 연결점 제거

    print(sum(dis)) #수신 가능 영역 거리의 합
