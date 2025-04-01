import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 1000000007

def main():
    def matrixMult(A, B):
        return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
                 (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
                [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
                 (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]]
    
    def matrixSquare(matrix, n):
        if n == 1:
            return [[1, 1], [1, 0]]
        
        half = matrixSquare(matrix, n//2)
        result = matrixMult(half, half)

        if n%2 == 1:
            result = matrixMult(result, matrix)
        
        return result

    n = int(input())
    print(matrixSquare([[1, 1], [1, 0]], n)[1][0])

main()