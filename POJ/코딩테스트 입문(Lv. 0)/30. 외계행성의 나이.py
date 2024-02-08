def solution(age):
    return ''.join(chr(int(s)+97) for s in str(age))