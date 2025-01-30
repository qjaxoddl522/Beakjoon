import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    def bt(idx, t1Score, t2Score):
        nonlocal result
        if idx == N:
            result = min(result, abs(t1Score-t2Score))
            return

        if len(t1) < N//2:
            newt1Score = t1Score
            t1.append(idx)
            for t in t1:
                newt1Score += score[idx][t] + score[t][idx]
            bt(idx+1, newt1Score, t2Score)
            t1.pop()
        
        if len(t2) < N//2:
            newt2Score = t2Score
            t2.append(idx)
            for t in t2:
                newt2Score += score[idx][t] + score[t][idx]
            bt(idx+1, t1Score, newt2Score)
            t2.pop()
        
    N = int(input())
    score = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')
    t1, t2 = [0], []
    bt(1, 0, 0)
    print(result)

main()