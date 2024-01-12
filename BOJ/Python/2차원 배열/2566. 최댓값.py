# 9 * 9 배열

# 1차원 배열로 입력 받기
arr = list(map(int, input().split()))
for i in range(8) :
    arr.extend(list(map(int, input().split())))

# 최대값 구하기 및 2차원일 때 index 구하기
print(max(arr))
print(arr.index(max(arr))//9+1, arr.index(max(arr))%9+1)
# 아래 코드를 참고해 수정한 부분
i = arr.index(M := max(arr))
print(M)
print(i//9+1, i%9+1)

## 다른 사람의 코드
# 표준 입력에서 숫자들을 읽어와서 리스트 L에 저장합니다.
# open(0)은 표준 입력을 연다. 0은 표준입력파일 디스크립터를 나타낸다
# read()는 파일을 읽어서 문자열로 변환한다
# *은 unpacking 이라고 하며, iterable의 요소를 풀어서 다른 iterable에 포함시키는 역할을 한다.
L = *map(int, open(0).read().split()),

# 리스트 L에서 최댓값을 찾아 M에 할당합니다.
# := 는 할당 표현식 또는 walrus 연산자로, 변수에 값을 할당하면서 동시에 그 값을 반환한다.
a = L.index(M := max(L))

# 최댓값 M과 해당 값의 인덱스를 1부터 시작하는 행 및 열로 변환하여 출력합니다.
print(M, a // 9 + 1, a % 9 + 1)