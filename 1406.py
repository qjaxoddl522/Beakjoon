import sys

str1 = list(sys.stdin.readline().rstrip()) #두개의 스택에 나눠서 담는다
str2 = []

for _ in range(int(sys.stdin.readline())):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == 'L':
        if str1: #비어있지 않으면 옮김
            str2.append(str1.pop())
    elif cmd[0] == 'D':
        if str2:
            str1.append(str2.pop())
    elif cmd[0] == 'B':
        if str1:
            str1.pop()
    else:
        str1.append(cmd[1])

str1.extend(reversed(str2))
print("".join(str1))
