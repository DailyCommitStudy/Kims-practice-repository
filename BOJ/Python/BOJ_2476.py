'''
1. 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
2. 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
3. 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
'''
case = list()

for _ in range(int(input())) :

    a, b, c = map(int, input().split())
    if (a == b == c) :
        case.append(10000 + a * 1000)
    elif (a == b or a == c) :
        case.append(1000 + a * 100)
    elif (b == c) :
        case.append(1000 + b * 100)
    else :
        case.append(max(a, b, c) * 100)

print(max(case))