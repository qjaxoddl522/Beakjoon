import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    while True:
        a, b, c = map(int, input().split())
        if a == 0 and b == 0 and c == 0:
            break

        # 등차수열
        if a-b == b-c and a-b != 0:
            print(f"AP {c + c - b}")
        # 등비수열
        else:
            print(f"GP {c * c // b}")

main()