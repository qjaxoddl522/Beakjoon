import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N, M = map(int, input().split())
    checker = [int(input()) for _ in range(N)]

    answer = 0
    s = 0
    e = sum(checker) * ((M//N)+1)
    while s <= e:
        mid = (s + e) // 2

        processed = 0
        for c in checker:
            processed += mid // c
        
        if processed >= M:
            e = mid - 1
            answer = mid
        else:
            s = mid + 1
    print(answer)

main()