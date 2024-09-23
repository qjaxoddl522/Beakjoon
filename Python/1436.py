n = int(input())
title = 0
while(n>0):
    title += 1
    stack = 0
    for i in str(title):
        if i == '6':
            stack += 1
            if stack == 3:
                n -= 1
                break
        else:
            stack = 0
print(title)
