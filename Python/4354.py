import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    while True:
        S = input()
        if S == ".":
            break

        fail = [0] * len(S)
        j = 0
        for i in range(1, len(S)):
            while j > 0 and S[i] != S[j]:
                j = fail[j-1]
            if S[i] == S[j]:
                j += 1
                fail[i] = j
        
        # fail[len(S)-1] = len(S)*(n-1)/n 을 만족
        if len(S) % (len(S) - fail[len(S)-1]) == 0:
            print(len(S) // (len(S) - fail[len(S)-1]))
        else:
            print(1)

main()