def solve(N, K):
    ans = 0
    
    sieve = set(range(2, N+1))
    erased = 0
    for i in range(2, N+1):
        # 아직 살아있으면 소수
        if i in sieve:
            # 배수는 지운다
            for j in range(i, N+1, i):
                if j in sieve:
                    sieve.remove(j)
                    erased += 1
                    if erased == K:
                        ans = j
                        return ans

N, K = map(int, input().split())
print(solve(N, K))
