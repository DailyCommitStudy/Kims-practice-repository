# 정석적인 방법
def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1

# 다른 사람 코드
'''
더 공부해보기
'''