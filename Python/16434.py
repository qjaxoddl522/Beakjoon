import math
import sys
input = sys.stdin.readline

N, attack = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

#최대 hp에 대한 이분탐색
bot, top = 1, sys.maxsize
ans = 0

while(bot <= top):
    mid = (bot + top) // 2
    maxHp, curHp = mid, mid #최대 체력, 현재 체력
    atk = attack #초기 공격력
    possible = True
    
    for r in room:
        if r[0] == 1: #몬스터
            monAtk = r[1]
            monHp = r[2]

            turn = (monHp // atk) if monHp % atk == 0 else (monHp // atk) + 1
            curHp -= monAtk * (turn - 1) #먼저 공격하므로 한 턴은 공짜

            if curHp <= 0: #사망
                possible = False
                break
            
        elif r[0] == 2: #포션
            atk += r[1]
            curHp = min(maxHp, curHp + r[2])

    if not possible:
        bot = mid + 1
    else:
        top = mid - 1
        ans = mid

print(ans)
