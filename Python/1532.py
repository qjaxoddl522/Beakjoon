import sys
input = lambda: sys.stdin.readline().rstrip()
import math

def main() -> None:
    G1, S1, B1 = map(int, input().split())
    G2, S2, B2 = map(int, input().split())
    result = 0
    
    # 동 부족
    if B2 > B1:
        needB = B2 - B1
        # 금을 은으로 바꾸기
        needS = max(0, math.ceil(needB / 9) - (S1 - S2))
        S1 += math.ceil(needS / 9) * 9
        G1 -= math.ceil(needS / 9)
        result += math.ceil(needS / 9)
        # 은을 동으로 바꾸기
        if (S1 - S2) * 9 >= needB:
            B1 += math.ceil(needB / 9) * 9
            S1 -= math.ceil(needB / 9)
            result += math.ceil(needB / 9)
    
    # 은 부족
    if S2 > S1:
        needS = S2 - S1
        # 남는 금을 은으로 바꾸기
        if G1 > G2:
            changeG = min(math.ceil(needS / 9), G1 - G2)
            S1 += changeG * 9
            G1 -= changeG
            result += changeG
        # 동을 은으로 바꾸기
        needS = max(0, S2- S1)
        if (B1 - B2) // 11 >= needS:
            S1 += needS
            B1 -= needS * 11
            result += needS
    
    # 금 부족
    if G2 > G1:
        needG = G2 - G1
        # 동을 은으로 바꾸기
        needS = max(0, needG * 11 - (S1 - S2))
        S1 += needS
        B1 -= needS * 11
        result += needS
        # 은을 금으로 바꾸기
        if (S1 - S2) // 11 >= needG:
            G1 += needG
            S1 -= needG * 11
            result += needG
    
    if G1 >= G2 and S1 >= S2 and B1 >= B2:
        print(result)
    else:
        print(-1)

main()