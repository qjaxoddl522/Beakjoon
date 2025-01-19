import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    ingredient = set()

    need = list(input().split())
    get = list(input().split())
    for name in get:
        ingredient.add(name)
    for name in need:
        if name not in ingredient:
            print(name)
            return

main()