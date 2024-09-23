import sys
input = sys.stdin.readline

N = int(input().rstrip())
word = [input().rstrip() for _ in range(N)]
value = {}

for w in word:
    l = len(w)-1
    for i in w:
        if i in value: #이미 값이 존재하면 더하기
            value[i] += 10**l
        else: #없으면 넣기
            value[i] = 10**l
        l -= 1

ans = 0
num = 9
#내림차순 크기 정렬 후 9부터 곱해서 답 출력
for i in sorted(value.values(), reverse=True):
    ans += num * i
    num -= 1
print(ans)
