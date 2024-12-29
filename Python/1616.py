import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    def de_bruijn(k, n):
        a = [0] * (k * n)  # 재귀에서 사용할 임시 배열
        sequence = []
        
        def db(t, p):
            if t > n:
                if n % p == 0:
                    # a[1 : p+1] 구간을 결과에 이어 붙인다.
                    sequence.extend(a[1:p+1])
            else:
                a[t] = a[t - p]
                db(t + 1, p)
                for j in range(a[t - p] + 1, k):
                    a[t] = j
                    db(t + 1, t)

        db(1, 1)
        return sequence

    K, M = map(int, input().split())
    seq = de_bruijn(K, M)
    print(*seq)

main()

# 실패
"""
def main():
    K, M = map(int, input().split())
    graph = dict()

    # M-1자리의 K진수를 전부 만든다
    dq = deque([0] * (M-1))
    for _ in range(K**(M-1)):
        # 첫 자리를 지우고 K-1까지 붙여 간선으로 연결
        node_tp = tuple(dq)
        deleted = dq.popleft()
        for i in range(K):
            dq.append(i)
            next_tp = tuple(dq)
            if node_tp not in graph:
                graph[node_tp] = dict()
            if next_tp not in graph[node_tp]:
                graph[node_tp][next_tp] = 0
            graph[node_tp][next_tp] += 1
            dq.pop()
        dq.appendleft(deleted)

        dq[-1] += 1
        for i in range(M-2, 0, -1):
            if dq[i] >= K:
                dq[i] = 0
                dq[i-1] += 1
            else:
                break
    
    #print('\n'.join(map(str, graph.items())))
    # DFS 수행
    stack = [(0,) * (M-1)]
    path = []
    while stack:
        node = stack[-1]
        if node in graph and graph[node]:
            for next, _ in graph[node].items():
                graph[node][next] -= 1
                if graph[node][next] == 0:
                    del graph[node][next]
                stack.append(next)
                break
        else:
            path.append(node)
            del stack[-1]
    
    result = []
    for i in range(len(path)-2, -1, -1):
        result.append(path[i][-1])
    print(*result)

main()
"""