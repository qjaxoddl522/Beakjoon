import sys
input = sys.stdin.readline

N, P = map(int, input().split())
stack = [[] for _ in range(6)]
ans = 0

for _ in range(N):
	melo = list(map(int, input().split()))
	
	while True:
		#해당 줄의 스택이 비어있거나 top이 더 작은 경우
		if not stack[melo[0] - 1] or stack[melo[0] - 1][-1] < melo[1]:
			stack[melo[0] - 1].append(melo[1])
			ans += 1
			break
		#top과 같은 경우
		elif stack[melo[0] - 1][-1] == melo[1]:
			break
		#top이 더 큰 경우
		elif stack[melo[0] - 1][-1] > melo[1]:
			stack[melo[0] - 1].pop()
			ans += 1
print(ans)
