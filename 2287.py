import sys
input = sys.stdin.readline

K = int(input())

#dp[i] = i개의 K를 써서 만들 수 있는 값들의 집합
dp = [set() for _ in range(9)]

#모두 붙어있는 숫자
for i in range(1, 9):
    dp[i].add(int(str(K)*i))

#i개의 K를 사용한 경우의 수 구하기
for i in range(2, 9):
    #양 변으로 나누어 경우의 수 계산(각 숫자의 길이)
    for n1 in range(1, i):
        n2 = i-n1

        for a in dp[n1]:
            for b in dp[n2]:
                dp[i].add(a+b)
                dp[i].add(abs(a-b))
                dp[i].add(a*b)
                #zeroDivision 방지
                if b > 0:
                    dp[i].add(a//b)

for _ in range(int(input())):
    target = int(input())
    
    #최소 길이 구하기
    ans = "NO"
    for i in range(1, 9):
        if target in dp[i]:
            ans = i
            break
    print(ans)
