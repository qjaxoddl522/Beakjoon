import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

#preorder를 기준으로 나누어가며 postorder
def post(start, end):
    #더 이상 나눌 수 없으면(자식이 없으면) 종료
    if start > end:
        return

    #루트보다 큰 값이 존재하지 않을 수 있음
    mid = end + 1
    for i in range(start + 1, end + 1):
        #루트보다 큰 값 찾으면 해당 값을 기준으로 나눔
        if preorder[start] < preorder[i]:
            mid = i
            break

    #후위순회 결과 출력
    post(start + 1, mid - 1)
    post(mid, end)
    print(preorder[start])

post(0, len(preorder) - 1)
