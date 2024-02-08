case = list()
for _ in range(7) :
    a = int(input())
    if a%2 == 1 : case.append(a)

if len(case) == 0 :
    print(-1)
else :
    print(sum(case))
    print(min(case))