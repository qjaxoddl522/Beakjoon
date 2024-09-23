line = sorted(list(map(int, input().split())))
rnd = line[0]+line[1]
if rnd <= line[2]:
    rnd += line[0]+line[1]-1
else:
    rnd += line[2]
print(rnd)
