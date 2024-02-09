# int로 변환 가능하면 true
# try - except 를 활용한 경우

def solution(s):
    if len(s) != 4 and len(s) != 6: return False
    try:
        s = int(s)
        return True
    except ValueError: return False

# 다른 사람 코드
def solution(s):
    return s.isdigit() and len(s) in [4, 6]