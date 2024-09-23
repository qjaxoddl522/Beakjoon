N, L = map(int, input().split())
loc = sorted(list(map(int, input().split())))

tape = 0 #필요한 테이프 수
tape_loc = 0 #현재 테이프를 붙일 위치
while(tape_loc < len(loc)):
    tape += 1
    for i in range(tape_loc, len(loc)):
        if loc[tape_loc]+(L-1) < loc[i]: #테이프가 더이상 닿지 않으면
            tape_loc = i #다음 테이프 준비
            break
        elif i == len(loc)-1: #전부 붙였으면 반복문 탈출
            tape_loc = len(loc)
print(tape)

