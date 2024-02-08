def solution(my_string):
    return sorted([int(i) for i in my_string if 48 <= ord(i) <= 57])

## 다른 사람 풀이
def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])