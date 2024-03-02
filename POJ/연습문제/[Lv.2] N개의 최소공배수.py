# n개의 수들의 배수 중 공통이 되는 가장 작은 숫자
# 탐색할 때... max(arr) ~ arr 속 모든 값들의 곱
from functools import reduce

def solution(arr):
    # max(arr) ~ arr 속 모든 값들의 곱
    for i in range(max(arr), reduce(lambda x, y: x*y, arr)+1):
        flag = True # 최소공배수인가?
        for n in arr: # arr 속 수에 대한 공통된 최소공배수인지 검사
            if i%n:
                flag = False # 최소공배수가 아니다
                break
        if flag: # 최소공배수면 바로 return
            return i
