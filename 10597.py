import sys
input = sys.stdin.readline
sys.setrecursionlimit(99999)

def backtrack(index): #현재 수열의 인덱스
    if index == len(seq):
        print(*ans, sep=' ')
        exit(0)

    #한 자리수: 0이 아니여야 하고 리스트에 없어야함
    if seq[index] != '0' and seq[index] not in ans:
        ans.append(seq[index])
        backtrack(index+1)
        ans.pop()

    #두 자리수: 10의 자리가 0이 아니여야 하고 리스트에 없어야 하고 n(최대 숫자)보다 작아야함
    if seq[index] != '0' and seq[index:index+2] not in ans and int(seq[index:index+2]) <= n:
        ans.append(seq[index:index+2])
        backtrack(index+2)
        ans.pop()

seq = input().rstrip()
#최대 숫자 구하기: 9자리 이하이면 수열 길이와 같고, 그보다 크면 9+나머지수열/2
n = len(seq) if len(seq) <= 9 else 9 + (len(seq) - 9) // 2
ans = []

backtrack(0)
