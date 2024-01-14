## 나의 풀이
# 파이썬이기 때문에 한 줄짜리의 간략한 코드가 나올 수 있었던 것 같다

def solution(array, commands):
    return [sorted(array[arr[0]-1:arr[1]])[arr[2]-1] for arr in commands]

## 다른 사람의 풀이 (1)
# 나와 유사하지만, for 문을 쓴 나와 달리 map과 lambda를 사용했다.
# 내가 반복 결과로 나오도록 하는 과정을 map 함수 속 실행 함수 lambda로 넣어 commands의 원소 하나하나에
# 적용할 수 있도록 했다.
# 내 풀이와 비교해서 어느것이 진정 효율적인지는 모르겠으나, 간지는 있는듯..

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

## 다른 사람의 풀이 (2)
# 나와 같은 로직? 이지만 보는 사람을 훨씬 잘 이해시킬 수 있는 코드
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer