import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
crane = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))

crane.sort(reverse=True)
box.sort(reverse=True)

result = 0

# 불가능
if crane[0] < box[0]:
    result = -1
# 가능
else:
    while box:
        for c in crane:
            # 옮길 수 있는 박스가 없음
            if box and c < box[-1]:
                continue
            # 옮길 수 있는 박스 중 가장 무거운 박스 선택
            for b in box:
                if c >= b:
                    box.remove(b)
                    break
        result += 1

print(result)
