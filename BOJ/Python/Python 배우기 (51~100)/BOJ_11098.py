## 첫번쨰 시도 >> 276ms

# for _ in range(int(input())) :
#     case = dict()
#     for _ in range(int(input())) :
#         k, v = input().split(' ')
#         case[int(k)] = v
#     print(case[max(case.keys())])

## 두번째 시도 >> 264ms
# 자료형의 유무가 중요한 건 아닌듯

# for _ in range(int(input())) :
#     p, n = list(), list()
#     for i in range(int(input())) :
#         a, b = input().split(' ')
#         p.append(int(a))
#         n.append(b)
#
#     print(n[p.index(max(p))])

## 세번째 시도 >> 260ms
for _ in range(int(input())) :
    max_p, max_n = 0, ''
    for _ in range(int(input())) :
        a, b = input().split(' ')
        if  max_p < int(a) : max_p, max_n = int(a), b

    print(max_n)