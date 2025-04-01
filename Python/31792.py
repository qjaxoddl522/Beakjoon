import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict
from bisect import bisect_left

def main():
    books = defaultdict(int)
    # 가격의 종류
    prices = []
    for _ in range(int(input())):
        cmd = list(map(int, input().split()))
        if cmd[0] == 1:
            if cmd[1] not in books:
                pricePos = bisect_left(prices, cmd[1])
                prices.insert(pricePos, cmd[1])
            books[cmd[1]] += 1
        elif cmd[0] == 2:
            if cmd[1] in books:
                books[cmd[1]] -= 1
                if books[cmd[1]] == 0:
                    del books[cmd[1]]
                    pos = bisect_left(prices, cmd[1])
                    prices.pop(pos)
        else:
            page = 0
            i = 0
            while i < len(prices):
                i = bisect_left(prices, prices[i]*2)
                page += 1
            print(page)

main()