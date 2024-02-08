# 아홉 개의 숫자 중 합이 100이 되는 일곱 개의 수를 찾기

def func() :
    case = [int(input()) for _ in range(9)]
    for i in range(9) :
        for j in range(i+1, 9) :
            if sum(case) - case[i] - case[j] == 100 :
                case.pop(i)
                case.pop(j-1)
                return '\n'.join(map(str, case))

print(func())
