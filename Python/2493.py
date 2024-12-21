import sys
input = lambda: sys.stdin.readline().rstrip()

def main() -> None:
    N = int(input())
    ls = list(map(int, input().split()))
    stack = []
    result = []
    for i in range(len(ls)):
        while stack and stack[-1][0] < ls[i]:
            stack.pop()
        if stack:
            result.append(stack[-1][1])
        else:
            result.append(0)
        stack.append((ls[i], i+1))
    print(*result)

main()