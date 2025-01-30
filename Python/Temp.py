a, b, c = map(int, input().split())
if a != b != c:
    print(max(a, b, c) * 100)
if a == b and b != c:
    print(1000 + (a * 100))
if a != b and b == c:
    print(1000 + (c * 100))
if a == c and a != b:
    print(1000 + (a * 100))
if a == b == c:
    print(10000 + (a * 1000))