N, K = map(int, input().split())
circle = ['?'] * N

for i in range(K):
    num, alpha = input().split()
    st = int(num) % N #한바퀴를 넘어갈 경우 나머지계산

    circle = circle[-st:] + circle[:-st] #시작지점 기준으로 슬라이싱

    if circle[0] == '?':
        if alpha in circle: #이미 다른 곳에 존재함
            print('!')
            break
        circle[0] = alpha
    elif circle[0] == alpha:
        continue
    else: #현재 자리에 다른 문자가 존재함
        print('!')
        break
else: #반복문 정상적으로 끝나면 출력
    print("".join(circle))
