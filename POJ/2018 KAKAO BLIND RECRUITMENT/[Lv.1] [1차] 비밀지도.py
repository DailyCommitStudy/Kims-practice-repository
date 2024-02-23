# arr1, arr2의 각 값을 5자리의 이진수로 변환 필요
# 각 변환된 값을 or 연산을 한 뒤 0은 ' ', 1은 #으로 변환 필요
# 자릿수를 맞출 때 format은 쓸 수 없다 -> 자릿수 맞추는 다른 로직 사용

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        m = bin(arr1[i] | arr2[i])[2:]  # 비트연산 결과
        m = "0" * (n - len(m)) + m  # 자릿수 맞추기

        # 1 -> #, 0 -> ' ' 으로
        m = m.replace("1", "#")
        m = m.replace("0", " ")

        answer.append(m)

    return answer

# 다른 사람 코드
# zip -> 데이터를 엮는 것이 목적인 함수 튜플 형태로! 두 가지 itrable 변수를 하나의 for문 안에 넣어 돌리고 싶을 때!!!
# rjust -> 오른쪽 정렬 후 공백을 메워줄 문자를 넣어준다 (처음봐요)
# rjust(오), ljust(왼), zfill(0을 왼쪽에)
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer