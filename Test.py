import itertools
import sys

def wrong(n, k, array):
    def binary_sort(array,k):
        #오름차순 정렬
        array.sort()
        #랜선 길이의 최소,최댓값,랜선 갯수,결과값 초기화
        start = 1
        end = array[-1] + 1
        result = 0

        while start < end:
            mid = (start+end) // 2
            count = 0
            
            for item in array:
                count += item // mid #랜선을 잘랐을때 갯수
            if count >= k:
                start = mid + 1
                result = mid
            else:
                end = mid - 1 
        return result

    answer = binary_sort(array,k)
    return answer

def correct(N, K, lan):
    bot, top = 1, max(lan)
    ans = 0

    while(bot <= top):
        mid = (bot + top) // 2
        n = 0
        for i in lan:
            n += i // mid

        if n >= N: #가능
            bot = mid + 1
            ans = mid
        else: #불가능
            top = mid - 1

    return ans

def findDiff():
    for k in range(5, 101):
        for n in range(k, 101):
            comb = list(itertools.combinations(range(1, 101), k))
            for tup in comb:
                ans_w = wrong(n, k, list(tup))
                ans_c = correct(n, k, list(tup))
                if ans_w != ans_c:
                    print(f"출력: {ans_w}")
                    print(f"정답: {ans_c}")
                    print(f"테스트케이스: {k}, {n}, {tup}")
                    break
    print("다른 테스트케이스를 찾지 못했습니다.")

findDiff()
