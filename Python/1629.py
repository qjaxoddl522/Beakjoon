def square(a, b, c):
    if b == 1:
        return a%c
    if b%2 == 0:
        return (square(a, b//2, c)**2)%c
    if b%2 == 1:
        return ((square(a, b//2, c)**2)*a)%c

A, B, C = map(int, input().split())
print(square(A, B, C))
