import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    for _ in range(int(input())):
        N = input()
        # 자릿수의 합
        hap = sum(map(int, N))
        
        if hap % 3 == 0:
            print(0, 3)
        elif hap % 3 == 1:
            idx = N.find('1')
            if idx != -1:
                print(idx+1, 3)
            else:
                # 전부 5로 구성되어 있으면 5의 배수
                print(0, 5)
        elif hap % 3 == 2:
            idx = N.find('5')
            if idx != -1:
                print(idx+1, 3)
            else:
                # 전부 1로 구성되어 있으면 11의 배수로 만들기
                if len(N) % 2 == 0:
                    print(0, 11)
                else:
                    print(1, 11)

main()