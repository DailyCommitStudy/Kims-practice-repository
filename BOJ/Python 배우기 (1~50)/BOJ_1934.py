## 1
# 시간초과로 실패
# import sys
# for _ in range(int(input())) :
#     A, B = sorted(map(int, sys.stdin.readline().split()))
#     i = B//A
#
#     while (A*i % B != 0) :
#         i += 1
#
#     print(A*i)

## 1
# A, B 최대공약수 * 최소공배수 = A * B
# 성공! 하지만 4260ms가 걸린다... 쩝~

for _ in range(int(input())) :
    A, B = sorted(map(int, input().split()))
    G = A

    for g in range(A, 0, -1) :
        if ((A%g == 0) and (B%g == 0)) :
            G = g
            break

    print(A * B // G)