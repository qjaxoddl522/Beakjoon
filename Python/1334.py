import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    def palindrome(string):
        if (len(string)) % 2 == 1:
            return string[0:len(string)//2] + string[len(string)//2] + string[0:len(string)//2][::-1]
        else:
            return string[0:len(string)//2] + string[0:len(string)//2][::-1]

    N = input()
    # 앞자리를 뒤집어서 뒷자리를 만들되, 원본 숫자보다 작으면 가운데 숫자를 + 방식으로 늘린다
    pal = palindrome(N)
    if int(N) >= int(pal):
        pal = palindrome(str(int(N) + 10**(len(N)//2)))

    print(pal)

main()