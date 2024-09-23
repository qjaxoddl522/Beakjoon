import sys
input = sys.stdin.readline

while(True):
    string = input().rstrip()
    if string == '#':
        break
    
    legal = True
    tagStack = []
    tagin = False #태그문자 입력중
    temp = '' #문자열 저장용
    
    for i in range(len(string)):		
        if string[i] == '<':
            tagin = True
        elif string[i] == '>':
            tagin = False
            #단일태그일 경우
            if temp and temp[-1] == '/':
                    temp = ''
                    continue
            #슬래시를 제외한 태그가 같을 경우
            elif tagStack and tagStack[-1] == temp[1:]:
                    tagStack.pop()
            #여는 태그면 태그추가
            else:
                    tagStack.append(temp)
            temp = ''
        elif tagin:
            #공백 다음에 슬래시가 없으면 속성이므로 태그 저장 제외
            if string[i] == ' ' and string[i+1] != '/':
                tagin = False
            else:
                temp += string[i]
    
    if tagStack or temp:
        print("illegal")
    else:
        print("legal")
