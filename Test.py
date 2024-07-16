month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while 1:
  # 입력
  D, M, Y = map(int, input().split())
  
  if D+M+Y==0: break
  
  # 풀이
  d = D
  if M>=2:
    d += sum(month[:M])
    if (Y%4==0 and Y%100!=0) or Y%400==0:
      d += 1

  # 출력
  print(d)
