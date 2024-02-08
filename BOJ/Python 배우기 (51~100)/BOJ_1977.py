
## 첫 번째 방법 -> 4396ms.. 먼디..ㅋ

# M = int(input())
# N = int(input())
#
# case = list()
# for i in range(M, N+1) :
#     for j in range(0, i+1) :
#         if (j*j == i) :
#             case.append(i)
#
# if (len(case) == 0) :
#     print(-1)
# else :
#     print(sum(case))
#     print(min(case))

## 두 번째 방법 -> 36ms, 다른 사람 코드 참고함
# 문제가 제시한 범위를 이용하면 더욱 효율적으로 할 수 있구나.. 디박..~!

M = int(input())
N = int(input())

case = [i*i for i in range(1, 101) if M <= i*i <= N ]

if (len(case) == 0) :
    print(-1)
else :
    print(sum(case))
    print(min(case))
