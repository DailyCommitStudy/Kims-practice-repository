## 임무를 시작한지 정확하게 24시간이 되는 순간
# 무조건 현재 < 시작한 시간
# 시작한 시간 - 현재 시간
# XX:XX:XX
# 00:00:00 ~ 23:59:59
# 만약 -가 되면 앞 인덱스를 -1(얘마저 마이너스가 되면 23으로) -> 60 + 그값

## 첫번째 시도
# st = list(map(int, input().split(':')))
# et = list(map(int, input().split(':')))
#
# rt = [et[i]-st[i] for i in range(3)]
#
# if rt[2] < 0 :
#     rt[2] += 60
#     rt[1] -= 1
# if rt[1] < 0:
#     rt[1] += 60
#     rt[0] -= 1
# if rt[0] < 0 :
#     rt[0] += 24
#
# print(f'{rt[0]:02}:{rt[1]:02}:{rt[2]:02}')


## 두번째 시도 -> 다른 사람 코드를 한 번 보고.. 결국 따라 써봄. 역시.. 사람은 수학을 잘해야..
def func() :
    h, m, s = map(int, input().split(':'))
    return h * 60 * 60 + m * 60 + s

rt = (-func()+func())%86400
print(f'{rt // 3600:02}:{rt // 60 % 60:02}:{rt % 60:02}')
