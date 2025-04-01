import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N, M, T = map(int, input().split())

    timeline = [[] for _ in range(T+1)]
    for i in range(1, N+1):
        a, b = map(int, input().split())
        timeline[a].append(i)
        timeline[b].append(-i)
    
    friend = [[] for _ in range(N+1)]
    for _ in range(M):
        c, d = map(int, input().split())
        friend[c].append(d)
        friend[d].append(c)
    
    # 대화 중인 사람들
    talking = set()
    # 즐거운 대화 중인 쌍의 수
    stack = 0
    for t in range(T):
        for i in timeline[t]:
            # 양수-입장 음수-퇴장
            if i > 0:
                for j in friend[i]:
                    if j in talking:
                        stack += 1
                talking.add(i)
            else:
                for j in friend[-i]:
                    if j in talking:
                        stack -= 1
                talking.remove(-i)
        print(stack)

main()