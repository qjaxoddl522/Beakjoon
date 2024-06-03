import sys
input = sys.stdin.readline

def solve():
    start = 0
    end = 0
    start_end_sum = ls[0]
    min_length = sys.maxsize

    #최대 길이까지
    while end < N:
        #기준치보다 작으면 끝점 올리기
        if start_end_sum < S:
            end += 1
            if end < N:
                start_end_sum += ls[end]
        #기준치보다 크면 시작점 올리기
        else:
            min_length = min(min_length, end - start + 1)
            start_end_sum -= ls[start]
            start += 1

    return min_length if min_length != sys.maxsize else 0

N, S = map(int, input().split())
ls = list(map(int, input().rstrip().split()))

print(solve())
