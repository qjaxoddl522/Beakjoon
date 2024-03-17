equation = list(input())
op = ('+', '-', '*', '/') #연산기호

stack = []
ans = ''

for e in equation:
    if e.isalpha():
        ans += e
    elif e in op:
        while True:
            if (not stack) or (stack[-1] == '(') or ((stack[-1] in op[:2]) and (e in op[2:])):
                stack.append(e)
                break
            else:
                ans += stack.pop()
    elif e == '(':
        stack.append(e)
    elif e == ')':
        while stack[-1] != '(':
            ans += stack.pop()
        stack.pop()
while stack:
    ans += stack.pop()

print(ans)
