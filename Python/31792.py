import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict
from bisect import bisect_left

def main():
    books = defaultdict(int)
    prices = []
    for _ in range(int(input())):
        cmd = list(map(int, input().split()))
        if cmd[0] == 1:
            if books[cmd[1]] == 0:
                pos = bisect_left(prices, cmd[1])
                prices.insert(pos, cmd[1])
            books[cmd[1]] += 1
        elif cmd[0] == 2:
            books[cmd[1]] -= 1
            if books[cmd[1]] == 0:
                pos = bisect_left(prices, cmd[1])
                if pos < len(prices) and prices[pos] == cmd[1]:
                    prices.pop(pos)
        else:
            print(prices)

main()