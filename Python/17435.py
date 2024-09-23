import sys
input = lambda: sys.stdin.readline().rstrip()

# 최대 500000번의 쿼리
MAX_J = 19 # 2^19 > 500001

m = int(input())
# func[i][j] = 정점 i에서 2^j번 이동 후의 정점 번호
func = [[-1] * MAX_J for _ in range(m+1)]
for i, j in enumerate(list(map(int, input().split()))):
    func[i+1][0] = j

# i에서 2^(j+1)번 이동한 후의 정점
# = i에서 2^j번을 두 번 이동한 후의 정점
# 그러므로 func[i][j] = func[next[i][j-1]][j-1]
for j in range(1, MAX_J):
    for i in range(1, m+1):
        func[i][j] = func[func[i][j-1]][j-1]

for _ in range(int(input())):
    n, x = map(int, input().split())
    # 켜져 있는 비트에 해당하는 배열만 사용
    for i in range(n.bit_length()-1, -1, -1):
        if n >= 1<<i:
            n -= 1<<i
            x = func[x][i]
    print(x)
