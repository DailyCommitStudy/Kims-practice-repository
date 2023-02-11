def solution(my_string, n):
    answer = my_string[0]*n
    for s in my_string[1:] :
        answer += s*n
    return answer

## 다른 사람 코드.. 이게되네 안될 줄 알았는데

def solution(my_string, n):
    return ''.join(i*n for i in my_string)