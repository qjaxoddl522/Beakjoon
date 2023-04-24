import sys
while(True):
    line = list(map(int, sys.stdin.readline().split()))
    line.sort()
    if line.count(0) == 3:
        break
    elif line[0]+line[1] <= line[2] :
        print("Invalid")
    elif line.count(line[0]) == 3:
        print("Equilateral")
    elif line.count(line[0]) == 2 or line.count(line[1]) == 2:
        print("Isosceles")
    else:
        print("Scalene")
