#기본 리스트 사용시 O(1) -> O(N)로 시간 복잡도 증가, 시간초과
from collections import deque

N = int(input())
card = deque(range(1, N+1))

while(len(card) > 1):
   card.popleft()
   card.append(card.popleft())

print(card[0])
