# ## 1 - 조건문 활용 > 36ms
# for _ in range(3) :
#     case = sum(map(int, input().split()))
#     if case == 3 : print('A')
#     elif case == 2 : print('B')
#     elif case == 1 : print('C')
#     elif case == 0 : print('D')
#     else : print('E')

# ## 2 - 리스트 인덱스 활용 > 60ms
# a = ['D', 'C', 'B', 'A', 'E']
# for _ in range(3) :
#     print(a[sum(map(int, input().split()))])

## 3 - 딕셔너리 활용 > 36ms
a = {0:'D', 1:'C', 2:'B', 3:'A', 4:'E'}
for _ in range(3) :
    print(a[sum(map(int, input().split()))])