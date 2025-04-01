import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    # 실질적인 행렬 제곱
    def matrix_mult(A, B):
        result = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % 1000
        return result

    # mat을 n번 제곱
    def matrix_power(mat, n):
        if n == 1:
            return matrix
        
        half = matrix_power(mat, n // 2)
        halfSquared = matrix_mult(half, half)
        
        if n % 2 == 0:
            return halfSquared
        else:
            return matrix_mult(halfSquared, mat)

    N, B = map(int, input().split())
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(N):
            matrix[i][j] = temp[j] % 1000

    for row in matrix_power(matrix, B):
        print(*row)

main()