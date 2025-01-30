import sys
input = lambda: sys.stdin.readline().rstrip()

def main() -> None:
    word = input()
    for i in range(len(word)//2):
        if word[i] != word[len(word)-i-1]:
            print(0)
            break
    else:
        print(1)
main()