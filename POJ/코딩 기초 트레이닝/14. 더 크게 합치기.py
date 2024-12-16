def merge(a, b):
    return int(str(a) + str(b))

def solution(a, b):
    ab = merge(a,b)
    ba = merge(b, a)
    return ab if ab >= ba else ba

# 다른 사람 풀이
# 그런데 문자열의 크기 비교와 숫자의 크기 비교에서 차이가 날까?
# 
def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))