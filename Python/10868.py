import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    def query(L, R, treeIdx, treeL, treeR):
        if R < treeL or treeR < L:
            return float('inf')
        if L <= treeL and treeR <= R:
            return tree[treeIdx]
        mid = (treeL + treeR) // 2
        return min(query(L, R, treeIdx*2, treeL, mid), query(L, R, treeIdx*2+1, mid+1, treeR))

    N, M = map(int, input().split())

    T = 1 << (N-1).bit_length()
    tree = [float('inf')] * (T*2)
    for i in range(T, T+N):
        tree[i] = int(input())
    for i in range(T-1, 0, -1):
        tree[i] = min(tree[i*2], tree[i*2+1])
    
    for _ in range(M):
        a, b = map(int, input().split())
        print(query(a-1, b-1, 1, 0, T-1))

main()