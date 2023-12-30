def loop(start, end):
    if start == end: #값이 하나면 바로 결과 도출
        return ls[start] * ls[start]

    mid = (start+end)//2 #중앙값
    result = max(loop(start, mid), loop(mid+1, end)) #중앙 기준 왼쪽과 오른쪽 중 더 높은 결과값 저장

    left = mid #확장하며 부분배열 확인하기 위함
    right = mid + 1
    summ = ls[left] + ls[right] #부분 배열 원소들의 합
    minn = min(ls[left], ls[right]) #부분 배열 원소들의 최소값
    result = max(result, minn * summ) #결과 최대값 갱신

    while (left > start) or (right < end): #리스트 범위제한
        if (right < end) and (left == start or ls[left-1] < ls[right + 1]): #원소값이 큰 쪽으로 확장 및 갱신
            right += 1
            summ += ls[right]
            minn = min(minn, ls[right])
        else:
            left -= 1
            summ += ls[left]
            minn = min(minn, ls[left])
        result = max(result, minn * summ)
    return result

N = int(input())
ls = list(map(int, input().split()))
print(loop(0, N-1))
