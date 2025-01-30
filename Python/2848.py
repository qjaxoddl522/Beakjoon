import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main() -> None:
    N = int(input())
    prevWord = ""
    graph = dict()
    inner = dict()
    for _ in range(N):
        word = input()
        for w in word:
            if w not in graph:
                graph[w] = set()
                inner[w] = 0
        if prevWord != "":
            for i in range(min(len(word), len(prevWord))):
                if word[i] != prevWord[i]:
                    if word[i] not in graph[prevWord[i]]:
                        graph[prevWord[i]].add(word[i])
                        inner[word[i]] += 1
                    break
            # 나중에 나온 문자열이 먼저 나온 문자열의 부분 문자열
            else:
                if len(prevWord) > len(word):
                    print("!")
                    return
        prevWord = word
    
    dq = deque()
    for w in inner.keys():
        if inner[w] == 0:
            dq.append(w)
    
    result = ""
    flag = False
    for _ in range(len(graph)):
        if len(dq) > 1:
            flag = True
        if not dq:
            print("!")
            return
        
        node = dq.popleft()
        result += node
        for next in graph[node]:
            inner[next] -= 1
            if inner[next] == 0:
                dq.append(next)
    else:
        print(result if not flag else "?")

main()
"""
3
aa
ab
b
위 반례에 주의
"""