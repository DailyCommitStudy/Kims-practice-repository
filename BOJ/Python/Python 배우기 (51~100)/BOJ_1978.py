n = int(input())
res = 0

for i in list(map(int, input().split())) :
    flag = True
    for j in range(2, i) :
        if i%j==0 : # 소수가 아닌 경우
            flag = False
            break
    if flag and 1 < i :
        res += 1

print(res)

## 소수라는 점 : 약수가 본인과 1 뿐이어야 함.
# 즉, 2~n-1 중 무엇으로 나누어도 나머지가 0이면 안됨

