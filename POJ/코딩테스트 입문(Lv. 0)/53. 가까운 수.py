def solution(array, n):
    array.sort()
    answer = array[0]
    for i in array[1:] :
        if abs(n-i) < abs(n-answer) : answer = i
    return answer

## 다른 사람 코드
# 정렬할 때 n과 차이나는 만큼을 key를 통해서 한 것.. x-n까지 있는 이유는 차이가 같으면 작은 값을 리턴해야 하니까!
def solution(array, n):
    array.sort(key = lambda x : (abs(x-n), x-n))
    answer = array[0]
    return answer