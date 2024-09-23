import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().rstrip().split())
array = list(input().rstrip().split())
visited = set(''.join(array)) #set은 문자열만 입력 가능함

target = sorted(array) #목표로 하는 정렬된 리스트

q = deque([[array, 0]]) #[현재 리스트, 횟수]
def bfs():
    ans = -1 #정답 횟수
    while q:
        arr, cnt = q.popleft()
        if arr == target:
            ans = cnt
            break
        for i in range(N-K+1): #i = 시작점
            rev_arr = list(reversed(arr[i:i+K]))
            new_arr = arr[:i] + rev_arr + arr[i+K:] #뒤집힌 리스트 합쳐서 재생성
            new_str = ''.join(new_arr)
            if new_str not in visited: #방문한 적 없는 set
                q.append([new_arr, cnt+1])
                visited.add(new_str)
    return ans

print(bfs())
