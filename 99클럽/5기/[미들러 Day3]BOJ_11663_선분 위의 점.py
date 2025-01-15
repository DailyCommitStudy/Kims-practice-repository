'''
점 N개와 선분 M개 ...
각각의 선분 위에 주어진 점이 몇 개 있는가?

N: 점의 개수, M: 선분의 개수 (1<= N, M <= 100,000)
두 점이 같은 좌표를 갖는 경우는 없다

N개 점의 좌표
M개 선분의 시작점과 끝점

1, 3, 10, 20, 30이 있으면
1 ~ 10 인 선분에는 3개
20 ~ 60 인 선분에는 2개?

선분의 시작점: a, 끝점: b
좌표 리스트에서 a 이상인 값 중 최솟값
b 이하인 값 중 최댓값 을 구해야 하는 건데..
그럼 앞뒤로 선형탐색을 하는 수밖에 없는 거 아냐?

그럼 a보다 큰 값 중 최솟값
b보다 작은 값 중 최댓값을 구한다?



if left가 a와 같을 때, a가 left보다 작을 때(a <= left) -> left
left == mid인 경우 -> mid

left가 a보다 작고 mid가 a보다 크다
right: mid/2-1

if right가 b와 같을 때, b가 right보다 클 때(b >= right) -> right
right == mid 인 경우 -> mid

'''

def find_left(target, arr):
    lower, upper = 0, len(arr)

    while lower < upper:
        middle = (lower + upper) // 2
        if  arr[middle] < target:
            lower = middle + 1
        else:
            upper = middle

    return lower

def find_right(target, arr):
    lower, upper = 0, len(arr)

    while lower < upper:
        middle = (lower + upper) // 2
        if arr[middle] <= target :
            lower = middle + 1
        else:
            upper = middle
            
    return lower

# 입력 데이터 저장
n, m = map(int, input().split(' '))
dots = sorted(map(int, input().split(' ')))
lines = [list(map(int, input().split(' '))) for _ in range(m)]

for a, b in lines:
    left = find_left(a, dots)
    right = find_right(b, dots) - 1

    if left <= right:
        print(right - left + 1)
    else:
        print(0)

# # 입력 데이터 저장
# n, m = map(int, input().split(' '))
# dots = list(map(int, input().split(' ')))
# lines = [list(map(int, input().split(' '))) for _ in range(m)]

# for line in lines:
#     a, b = line

#     # a가 dot[-1] 보다 큰 경우
#     # b가 dot[0] 보다 작은 경우
#     if a > dots[-1] or b < dots[0]:
#         print(0)
#         continue

#     for i in range(n):
#         if a <= dots[i]:
#             break
    
#     for j in range(n-1, -1, -1):
#         if b >= dots[j]:
#             break

#     print(j-i+1)