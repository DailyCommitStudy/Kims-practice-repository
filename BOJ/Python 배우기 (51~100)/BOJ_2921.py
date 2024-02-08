# 세트의 크기가 N인 도미노 속 점 개수는 0 <= 개수 <= N
# 찍힌 것이 같으면 같은 것.
# 2면, 0+0, 0+1, 1+1, 0+2, 1+2, 2+2
# 0 1 2 a0 a1 a2
# 0 1 2 b0 b1 b2
# a0 + b1 = a1 + b2

n = int(input())
res = 0

for i in range(n+1) :
    for j in range(n+1) :
        if i <= j :
            res += i+j

print(res)