x = input()
ls = []
while x not in ls:
    ls.append(x)
    x = str(int(x[0]) * len(x))
if x == ls[-1]:
    print('FA')
else:
    print('NFA')
