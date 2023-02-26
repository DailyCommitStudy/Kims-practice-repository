def solution(array):
    answer = 0
    for i in array :
        answer += str(i).count('7')
    return answer

## 이게되네
def solution(array):
    return str(array).count('7')