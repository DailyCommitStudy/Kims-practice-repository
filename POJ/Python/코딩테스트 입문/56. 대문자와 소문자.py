def solution(my_string):
    answer = ''
    for c in my_string :
        if 65 <= ord(c) <= 90 : answer += chr((ord(c)+32))
        else : answer += chr((ord(c)-32))
    return answer

# 이렇게 함수를 쓸 수도 있군
def solution(my_string):
    answer = ''
    for c in my_string :
        if 65 <= ord(c) <= 90 : answer += c.lower()
        else : answer += c.upper()
    return answer