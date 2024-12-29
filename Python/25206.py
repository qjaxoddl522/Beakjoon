import sys
input = lambda: sys.stdin.readline().rstrip()

score = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0, 'P':0.0}
summ = 0
subs = 0
for _ in range(20):
    _, major, sc = input().split()
    if sc != 'P':
        summ += float(major) * score[sc]
        subs += float(major)
print(summ/subs)