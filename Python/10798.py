arr = []
for _ in range(5):
    arr.append(input())
for i in range(len(max(arr, key=len))):
    for j in range(5):
        if len(arr[j]) > i:
            print(arr[j][i], end="")
"""
입력
ABCDE
abcde
01234
FGHIJ
fghij

출력
Aa0FfBb1GgCc2HhDd3IiEe4Jj

입력
AABCDD
afzz
09121
a8EWg6
P5h3kx

출력
Aa0aPAf985Bz1EhCz2W3D1gkD6x
"""
