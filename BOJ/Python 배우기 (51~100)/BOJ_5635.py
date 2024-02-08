## 첫번째 시도
# max_case = list()
# min_case = list()
#
# T = int(input())
# for i in range(T) :
#     case = input().split(' ')
#     case[1:] = [int(i) for i in case[1:]]
#
#     if i == 0 :
#         max_case = case.copy()
#         min_case = case.copy()
#         continue
#
#     if (min_case[3] < case[3]):  # 나이가 적은지
#         min_case = case.copy()
#     elif max_case[3] > case[3] : # 가장 나이가 많은지
#         max_case = case.copy()
#
#     elif min_case[3] == case[3]:
#         if min_case[2] < case[2] :
#             min_case = case.copy()
#         elif min_case[2] == case[2] and min_case[1] < case[1] :
#             min_case = case.copy()
#
#     elif max_case[3] == case[3]:
#         if max_case[2] > case[2] :
#             max_case = case.copy()
#         elif max_case[2] == case[2] and max_case[1] > case[1] :
#             max_case = case.copy()
#
# print(min_case[0])
# print(max_case[0])

## 다른 사람 정답 보고 안 것. lambda와 정렬 함수를 공부하고 나니 이해가 된다.. 세상에..
n = int(input())
a = []
for i in range(n):
    b = list(input().split())
    for i in range(1,4):
        b[i] = int(b[i])
    a.append(b)
print(a)
# 이차원으로 이름, 일, 월, 연도가 저장된 리스트를 연도, 월, 일 순으로 오름차순 정렬을 진행함.
a.sort(key = lambda x: (x[3],x[2],x[1]))
print(a)

print(a[-1][0])
print(a[0][0])