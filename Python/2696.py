import sys, math
input = sys.stdin.readline
import heapq as hq

for _ in range(int(input())):
    maxHeap = [] #top이 K-1번째 수(최대 힙은 음수연산)
    minHeap = [] #top이 K+1번째 수
    mid = None #중앙값
    
    M = int(input())
    m = 0 #수의 개수

    print(math.ceil(M/2), end='')
    for _ in range((M//10)+1):
        ls = list(map(int, input().rstrip().split()))
        for n in ls:
            m += 1            
            #수의 개수가
            #짝수면 중앙값을 기준으로 분배
            if m%2 == 0:
                if n < mid:
                    hq.heappush(maxHeap, -n)
                    hq.heappush(minHeap, mid)
                else:
                    hq.heappush(maxHeap, -mid)
                    hq.heappush(minHeap, n)
            #홀수면 최소힙 top을 기준으로 분배
            elif m%2 == 1:
                #첫 숫자면 중앙값
                if mid == None:
                    mid = n
                elif n > minHeap[0]:
                    hq.heappush(minHeap, n)
                    mid = hq.heappop(minHeap)
                else:
                    hq.heappush(maxHeap, -n)
                    mid = hq.heappop(maxHeap) * -1

                #줄넘김
                if m%20 == 1:
                    print()
                print(mid, end=' ')
    print()
