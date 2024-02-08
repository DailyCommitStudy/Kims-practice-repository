def solution(my_string):
    my_string = list(my_string)[::-1]
    for c in set(my_string) :
        while my_string.count(c) > 1:
            my_string.remove(c)
    return ''.join(my_string[::-1])

print(solution("people"))

# 2
def solution(my_string):
    answer = ''
    for c in my_string :
        if c not in answer :
            answer += c
    return answer