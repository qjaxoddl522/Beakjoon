import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(int(1e9))

# 메모이제이션을 위한 딕셔너리
memo = {}

# (길이, 합, 다음 시작 숫자(오름차순 유지))
def count_sequences(n, m, start):
    if n == 0:
        return 1 if m == 0 else 0
    if (n, m, start) in memo:
        return memo[(n, m, start)]
    
    count = 0
    for i in range(start, m // n + 1):
        count += count_sequences(n - 1, m - i, i)
    
    memo[(n, m, start)] = count
    return count

# K번째 수열을 찾기 위한 DFS
def find_kth_sequence(n, m, start, k):
    if n == 0:
        return []
    
    for i in range(start, m // n + 1):
        cnt = count_sequences(n - 1, m - i, i)
        if k <= cnt:
            return [i] + find_kth_sequence(n - 1, m - i, i, k)
        k -= cnt

# 길이, 합, K번째 수
N, M, K = map(int, input().split())

# K번째 수열 찾기
sequence = find_kth_sequence(N, M, 1, K)
print(*sequence)
