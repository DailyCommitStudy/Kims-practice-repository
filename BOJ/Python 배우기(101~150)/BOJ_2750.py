# ## 첫번째 방법 >> 156ms >> 반복문을 너무 많이 쓰나?
# case = sorted([int(input()) for _ in range(int(input()))])
# for c in case : print(c)

## 두번쨰 방법 >> 출력할 때 반복문을 쓰지 않으면서 추가적으로 함수 사용(list, map)
# >> 92ms
case = list(map(str, sorted([int(input()) for _ in range(int(input()))])))
print('\n'.join(case))