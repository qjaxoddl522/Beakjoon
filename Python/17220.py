import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    def dfs(node):
        result = 0
        for next in graph[node]:
            if not visited[next] and next not in excepted:
                visited[next] = True
                result += dfs(next) + 1
        return result

    N, M = map(int, input().split())
    init = set(range(N))
    graph = [[] for _ in range(N)]
    for _ in range(M):
        s, e = input().split()
        sIdx, eIdx = ord(s)-ord('A'), ord(e)-ord('A')
        graph[sIdx].append(eIdx)
        init.discard(eIdx)
    excepted = set(map(lambda s: ord(s)-ord('A'), input().split()[1:]))

    visited = [False] * N
    answer = 0
    while init:
        st = init.pop()
        if st not in excepted:
            answer += dfs(st)
    print(answer)

main()