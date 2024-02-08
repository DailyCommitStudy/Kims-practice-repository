def solution(my_string, letter):
    return ''.join(s for s in my_string if letter != s)

## 아맞다 replace
def solution(my_string, letter):
    return my_string.replace(letter, '')