# 시간이 너무 오래걸리네... -> 4316ms

# 1. 나이오름차순
# 2. 가입한 순서 오름차순

case = [[i, input().split()] for i in range(int(input()))]
case.sort(key=lambda x: (int(x[1][0]), x[0]))

for c in case:
    print(c[1][0], c[1][1])