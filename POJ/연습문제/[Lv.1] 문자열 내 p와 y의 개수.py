def solution(s):
    s = s.upper()
    return False if s.count("P") != s.count("Y") else True

## 다른 사람의 코드
def solution(s):
    return s.upper().count("P") == s.upper().count("Y")
