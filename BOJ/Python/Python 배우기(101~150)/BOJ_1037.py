# a에 있는 수의 공통된 배수여야 함. a는 1 < a < n
# 가장 작은 것과 큰 것을 곱하면 됨!

n = int(input())
a = sorted(map(int, input().split()))
print(a[0]*a[-1])