import sys
angle = [int(sys.stdin.readline()) for _ in range(3)]
if sum(angle) != 180:
    print("Error")
elif angle.count(60) == 3:
    print("Equilateral")
elif angle.count(angle[0]) == 2 or angle.count(angle[1]) == 2:
    print("Isosceles")
else:
    print("Scalene")
