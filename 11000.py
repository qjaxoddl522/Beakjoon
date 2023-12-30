import heapq

N = int(input())
ST = [list(map(int, input().split())) for _ in range(N)]
ST.sort(key = lambda x: (x[0], x[1]))

room = []
heapq.heappush(room, ST[0][1]) #첫타임 힙푸시

for i in range(1, N):
    if ST[i][0] >= room[0]: #존재하는 회의실이 사용 가능할경우
        heapq.heappop(room) #시간 변경을 위해 pop후 push
        heapq.heappush(room, ST[i][1])
    else: #현재 회의실 종료시간보다 다음 회의 시작시간이 빠르면
        heapq.heappush(room, ST[i][1]) #새로운 회의실 push
print(len(room))

"""
room = [0] #강의실 사용 종료시간
for i, j in ST:
    for k in range(len(room)):
        if room[k] <= i:
            room[k] = j
            break
        elif k == len(room)-1: #가능한 시간이 없으면 방 추가
            room.append(j)
print(len(room))

#시간초과
"""
