## 좀 더 효율적인 코드가 있을 것 같은데..

a = int(input())
b = int(input())

sum = 0
m = b

for i in range(a, b+1) :
    flag = True
    for j in range(2, i) :
        if i%j==0 : # 소수가 아닌 경우
            flag = False
            break
    if flag and 1 < i :
        sum += i
        if i < m : m = i

if sum == 0 : print(-1)
else :
    print(sum)
    print(m)