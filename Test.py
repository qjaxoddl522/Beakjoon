N, K = map(int, input().split())
A = list(map(int, input().split()))
b = 0 
c = 0
count = 0

while count < N and c != N-1:
    if A[c+1]-A[c] <K:
        c = c
        count +=1
    elif A[c+1]-A[c]>=K:
        c = c+1
        count +=1

for i in range(N):
    b +=A[c]+K*(i-c) -A[i]

print(b)
