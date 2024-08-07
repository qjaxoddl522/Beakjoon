import sys
input = lambda: sys.stdin.readline().rstrip()

# 맨 앞자리가 아닌 6을 0으로
def replace(s):
    first = s[0]
    other = s[1:]

    other = other.replace('6', '0')
    return first + other

def solve():
    n = int(input())
    
    # 가장 큰 수는 111.. 또는 711.. 이다
    maxNum = str('7'*(n%2)) + ('1'*(n//2-int(n%2==1)))
    minNum = dp[n]

    print(minNum, maxNum)

# dp[i] = i개의 성냥개비로 만들 수 있는 가장 작은 수
dp = [float('inf')] * 101
# 기본값
dp[2], dp[3], dp[4], dp[5], dp[6], dp[7] =\
       1, 7, 4, 2, 6, 8

for i in range(8, 101):
    for j in range(2, i-1):
        dp[i] = min(dp[i],\
                    int(replace(str(dp[i-j]) + str(dp[j]))))

for _ in range(int(input())):
    solve()
