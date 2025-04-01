import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n, L = map(int, input().split())
    box = list(map(int, input().split()))

    total = 0
    for i in range(n-1, 0, -1):
        total += box[i]
        if not (box[i-1]-L < total/(n-i) < box[i-1]+L):
            print("unstable")
            return
    print("stable")

main()