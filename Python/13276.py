import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    def find(P):
        fail = [0] * len(P)
        j = 0
        for i in range(1, len(P)):
            while j > 0 and P[i] != P[j]:
                j = fail[j-1]
            if P[i] == P[j]:
                j += 1
                fail[i] = j

        result = []
        j = 0
        for i in range(len(S)):
            while j > 0 and S[i] != P[j]:
                j = fail[j-1]
            if S[i] == P[j]:
                if j == len(P)-1:
                    result.append(i-len(P)+1)
                    j = fail[j]
                else:
                    j += 1
        
        return result
    
    S = input()
    A = input()
    B = input()
    
    idxA = find(A)
    idxB = find(B)
    word = set()
    for b in idxB:
        for a in idxA:
            # a의 시작과 b의 시작, a의 끝과 b의 끝이 유효한지 확인
            if a > b or a+len(A) > b+len(B):
                break
            word.add(S[a:b+len(B)])
    print(len(word))

main()