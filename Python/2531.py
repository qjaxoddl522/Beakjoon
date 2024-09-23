import sys
input = lambda: sys.stdin.readline().rstrip()

N, d, k, c = map(int, input().split())
rotate = [int(input()) for _ in range(N)]

selected = {c:1}
for n in rotate[:k]:
    if n in selected:
        selected[n] += 1
    else:
        selected[n] = 1

ans = len(selected)
for s in range(N):
    if ans == k+1:
        break

    if selected[rotate[s]] > 1:
        selected[rotate[s]] -= 1
    else:
        del selected[rotate[s]]
    
    e = (s + k) % N
    if rotate[e] in selected:
        selected[rotate[e]] += 1
    else:
        selected[rotate[e]] = 1

    ans = max(ans, len(selected))

print(ans)