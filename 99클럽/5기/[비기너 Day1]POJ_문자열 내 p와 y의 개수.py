def solution(s):
    s = s.upper()
    return False if s.count("P") != s.count("Y") else True