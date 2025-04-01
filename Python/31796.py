import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    S = sorted(list(map(int, input().split())))
    page = 0
    # 현재 페이지에서 수용 가능한 최대 가격
    nowMax = 0
    for p in S:
        if nowMax <= p:
            nowMax = p * 2
            page += 1
    print(page)

main()