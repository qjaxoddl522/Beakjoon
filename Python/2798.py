n, m = map(int, input().split())
card = list(map(int, input().split()))
result = 0
for i in card:
    for j in card:
        for k in card:
            if not(i==j or j==k or i==k):
                if m >= i+j+k and result < i+j+k:
                    result = i+j+k
print(result)
