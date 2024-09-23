import sys
sys.setrecursionlimit(99999)
input = sys.stdin.readline

def isVowel(alphabet):
    return (alphabet in ('a', 'e', 'i', 'o', 'u'))

def dfs(pos, prev, consonant, vowel): #현재 바꿀 문자 위치, 암호 시험해볼 문자 시작 위치, 자음 개수, 모음 개수
    global key
    #암호 조건 만족
    if (pos == L and consonant >= 2 and vowel >= 1):
        print(''.join(key[:L]))
        return

    #아직 사용하지 않은 암호들 시도
    for i in range(prev+1, C):
        key[pos] = alp[i]
        dfs(pos+1, i, consonant + (not isVowel(alp[i])), vowel + (isVowel(alp[i])))

L, C = map(int, input().rstrip().split())
alp = sorted(list(input().rstrip().split()))
key = [''] * 16
dfs(0, -1, 0, 0)
