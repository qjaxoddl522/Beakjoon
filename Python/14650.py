import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    def bt(length, hap):
        nonlocal answer
        if length >= N:
            if hap % 3 == 0:
                answer += 1
            return
        
        for i in range(3):
            if length == 0 and i == 0:
                continue
            bt(length+1, hap+i)
    
    N = int(input())
    answer = 0
    bt(0, 0)
    print(answer)

main()