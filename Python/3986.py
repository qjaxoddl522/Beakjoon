import sys
input = sys.stdin.readline

N = int(input())
ans = 0

for _ in range(N):
	word = input().rstrip()
	
	stack = []
	for w in word:
		#스택이 비어있거나 탑이 다르면 추가
		if not stack or stack[-1] != w:
			stack.append(w)
		#탑이 같으면 pop
		elif stack[-1] == w:
			stack.pop()
	
	#스택이 비어있으면 좋은단어
	if not stack:
		ans += 1

print(ans)
