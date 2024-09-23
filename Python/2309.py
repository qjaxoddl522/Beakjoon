n = [int(input()) for _ in range(9)]
breaker = False
for i in n:
    for j in n:
        if i != j:
            if sum([k for k in n if k not in {i,j}]) == 100: #제외할 숫자
                n.remove(i)
                n.remove(j)
                breaker = True
                break
    if breaker:
        break

for i in sorted(n): #출력
    print(i)
