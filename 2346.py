N = int(input())
balloon = list(map(int, input().split()))

idx = 0
order = []

for i in range(N-1):
    move = balloon[idx]
    order.append(idx + 1)
    balloon[idx] = 0
    while(move != 0):
        if move > 0:
            idx = (idx + 1) % len(balloon)
            if balloon[idx] != 0:
                move -= 1
        elif move < 0:
            idx = (idx - 1) % len(balloon)
            if balloon[idx] != 0:
                move += 1
order.append(idx + 1)
print(" ".join(map(str, order)))
