## 내가 짠 코드
# 꽤나 무식한 방법인듯. 그냥 count로 숫자를 셈. 끝.
def solution(array):
    array_set = list(set(array))
    array_count = [array.count(i) for i in array_set]
    if array_count.count(max(array_count)) > 1:
        return -1
    else:
        return array_set[array_count.index(max(array_count))]

## 다른 사람의 코드
# set()을 활용해서 계속 array의 값을 지우는데 결국 for을 다 돌았을 때 i가 0이면 배열에 하나의 숫자만 남았다는 뜻.
# 즉, 최빈값이라는 뜻이므로 return.
# 배열의 크기가 0이 되어도 마지막으로 for문을 돌고 i가 0이 아니라면 최빈값이 둘 이상이었단 뜻
# 개 똑똑해 ㅁㅊ

def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            print(i, a, set(array), array)
            array.remove(a)
        if i == 0: return a
        print(set(array), array)
    return -1

print(solution([0,1,0,1,0,1,0,2,1,0,2,0]))