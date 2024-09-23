n = int(input())
gigle = []
for _ in range(n):
    name, state = input().split()
    if state == 'enter':
        gigle.append(name)
    elif state == 'leave':
        gigle.remove(name)
for name in sorted(gigle, reverse=True):
    print(name)
