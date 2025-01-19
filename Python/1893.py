import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    for _ in range(int(input())):
        A = input()
        W = input()
        S = input()
        dic = {A[i]:i for i in range(len(A))}
        w = len(W)
        s = len(S)

        fail = [0] * w
        j = 0
        for i in range(1, w):
            while j > 0 and W[i] != W[j]:
                j = fail[j-1]
            if W[i] == W[j]:
                j += 1
                fail[i] = j
        
        result = []
        for shift in range(len(A)):
            # 검색한 W의 개수
            search = 0
            j = 0
            for i in range(s):
                while j > 0 and A[(dic[S[i]]-shift)%len(A)] != W[j]:
                    j = fail[j-1]
                if A[(dic[S[i]]-shift)%len(A)] == W[j]:
                    if j == w-1:
                        search += 1
                        j = fail[j]
                    else:
                        j += 1
            if search == 1:
                result.append(shift)

        if len(result) == 0:
            print("no solution")
        elif len(result) == 1:
            print(f"unique: {result[0]}")
        elif len(result) > 1:
            print("ambiguous:", *result)

main()