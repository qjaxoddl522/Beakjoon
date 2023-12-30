N = int(input())
meeting = [list(map(int, input().split())) for _ in range(N)]
meeting.sort(key=lambda x: (x[1], x[0])) #오름차순 정렬

end, result = 0, 0
for i, j in meeting:
    if end <= i: #끝나는 시간이 가장 빠른 회의부터 진행
        result += 1
        end = j
print(result)
