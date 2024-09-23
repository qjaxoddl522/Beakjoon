import sys
input = sys.stdin.readline

N = int(input())
equation = list(input().rstrip())
num = [int(input()) for _ in range(N)]

stack = [] #후위표기식 계산을 위한 스택

for e in equation:
    if e.isalpha():
        stack.append(num[ord(e)-65])
    else:
        b = stack.pop()
        a = stack.pop()

        if e == '+':
            stack.append(a+b)
        elif e == '-':
            stack.append(a-b)
        elif e == '*':
            stack.append(a*b)
        elif e == '/':
            stack.append(a/b)
print("{:.2f}".format(stack[0]))
