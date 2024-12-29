import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    a, b, c = map(int, input().split())

    # 일단 상관 없는 사람들이 필요한 수 만큼 채워준다
    needa = (3-a%3)%3
    needb = (4-b%4)%4
    c -= needa + needb
    if c < 0:
        print(-1)
        return

    table_three = a//3 + (1 if a%3 != 0 else 0)
    table_four = b//4 + (1 if b%4 != 0 else 0)

    # 남은 상관 없는 사람들로 테이블 채우기
    while c%4 != 0 and c >= 3:
        c -= 3
        table_three += 1
    if c%4 != 0:
        print(-1)
        return
    table_four += c//4
    print(table_three, table_four)

main()