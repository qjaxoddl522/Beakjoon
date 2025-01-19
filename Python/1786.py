import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    T = input()
    P = input()

    fail = [0] * len(P)
    j = 0
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = fail[j-1]
        if P[i] == P[j]:
            j += 1
            fail[i] = j

    # 문자열 찾기
    result = []
    j = 0
    for i in range(len(T)):
        while j > 0 and T[i] != P[j]:
            j = fail[j-1]
        if T[i] == P[j]:
            if j == len(P)-1:
                result.append(i-len(P)+2)
                j = fail[j]
            else:
                j += 1
    
    print(len(result))
    for i in result:
        print(i)

main()