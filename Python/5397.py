import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    str1 = [] #커서를 기준으로 두개의 스택에 나눠서 담는다
    str2 = []
    
    cmd = list(input().rstrip())
    for c in cmd:
        if c == '-':
            if str1: #비어있지 않으면
                str1.pop()
        elif c == '<':
            if str1:
                str2.append(str1.pop())
        elif c == '>':
            if str2:
                str1.append(str2.pop())
        else:
            str1.append(c)
    str1.extend(reversed(str2))
    print("".join(str1))
