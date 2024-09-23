import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(str):
    result = 0
    par = []
    num = 1
    for i in range(len(str)):
        if str[i] == '(':
            par.append(str[i])
            num *= 2
        if str[i] == ')':
            if not par or par[-1] != '(':
                return 0
            if str[i-1] == '(':
                result += num
            par.pop()
            num //= 2
        
        if str[i] == '[':
            par.append(str[i])
            num *= 3
        if str[i] == ']':
            if not par or par[-1] != '[':
                return 0
            if str[i-1] == '[':
                result += num
            par.pop()
            num //= 3
    return result if not par else 0

print(solve(input()))