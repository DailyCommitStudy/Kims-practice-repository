## 평균, 최빈값

case = [int(input()) for _ in range(10)]
cou = [case.count(i) for i in case]
print(sum(case)//10)
print(case[cou.index(max(cou))])