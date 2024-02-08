## 24.01.28) 121528KB, 653ms
# 기본 라이브러리 쓰는 것 말고 어떤 좋은 방법이 있을지?

# 숫자 카드 N개, 정수 M개
# 그 수가 적혀있는 숫자 카드를 상근이가 갖고 있는지 아닌지

N = int(input())
n = set(map(int, input().split()))

M = int(input())
m = list(map(int, input().split()))

for i in m :
    if i in n : print(1, end=' ')
    else : print(0, end=' ')