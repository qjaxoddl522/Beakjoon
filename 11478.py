import sys
input = sys.stdin.readline

word = input().rstrip()

res = []
for i in range(1, len(word)+1):
    for j in range(len(word)-i+1):
        res.append(word[j:j+i])
print(len(set(res)))
