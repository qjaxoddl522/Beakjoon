import sys
input = sys.stdin.readline

def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)
    if root1 != root2:
        root[root2] = root1
        num[root1] += num[root2]
    print(num[root1])

def find(node):
    if node != root[node]:
        root[node] = find(root[node])
    return root[node]

for _ in range(int(input())):
    #부모, 집합의 크기
    root, num = {}, {}
    F = int(input())
    for _ in range(F):
        name1, name2 = input().split()
        if name1 not in root:
            root[name1] = name1
            num[name1] = 1
        if name2 not in root:
            root[name2] = name2
            num[name2] = 1
        union(name1, name2)
    #print(root, num)
