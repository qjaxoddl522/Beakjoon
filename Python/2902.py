import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    string = input()
    result = string[0]
    for i in range(len(string)):
        if string[i] == "-":
            result += string[i+1]
    print(result)

main()