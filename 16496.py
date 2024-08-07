import sys
input = lambda: sys.stdin.readline().rstrip()
from functools import cmp_to_key

def compare(a, b):
    if a+b > b+a:
        # 그대로
        return -1
    else:
        # 자리 변경
        return 1

N = int(input())
ls = list(input().split())

# 맨 앞자리를 기준으로 숫자들을 나눈다
first_ls = [[] for _ in range(10)]
for n in ls:
    first_ls[int(n[0])].append(n)

# 조건 정렬
for i in range(len(first_ls)):
    first_ls[i].sort(key=cmp_to_key(compare))

result = ''
for i in range(len(first_ls)-1, -1, -1):
    for j in first_ls[i]:
        result += j
print(int(result))
