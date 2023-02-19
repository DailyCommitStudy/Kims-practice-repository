# 1. replace 활용
def solution(my_string):
    for i in ['a', 'e', 'i', 'o', 'u'] :
        my_string = my_string.replace(i, '')
    return my_string

# 2. for - if 사용
def solution(my_string):
    return ''.join(i for i in my_string if i not in 'aeiou')