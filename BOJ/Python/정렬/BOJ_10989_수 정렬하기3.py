'''
# 수 정렬하기 2 코드에서 추가 수정
import sys
case = [int(sys.stdin.readline()) for i in range(int(input()))]
for c in case : print(c)

문제 조건에 따르면 많은 숫자를 리스트에 하나하나 담고 계산하기엔 무리가 있다.
따라서 카운트배열로 범위의 숫자가 있는 리스트를 만들고 카운트를 하도록 했다.
-> 6780ms, 31120KB로 1차 성공
카운트 값이 0보다 클 때만 반복하도록
-> 7240ms, 31120KB로 2차 성공 근데 조건문 때문인지 시간이 더 걸리네.. 그냥 안하는 게 나은듯
'''

import sys

N = int(sys.stdin.readline())
arr = [0] * 10001
for _ in range(N):
    arr[int(sys.stdin.readline())] += 1
for i in range(10001) :
    for j in range(arr[i]):
        sys.stdout.write((str(i)+'\n'))