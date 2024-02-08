# 6개의 경우 모두 기울기를 구한다.
# 기울기가 같은 게 존재하는지 비교한다.
# abcd, ab 01 - cd 23 / ac 02 - bd 13 / ad 03 - bc 12
# 기울기 공식 y2-y1 / x2-x1

def func(a, b) :
    return (a[1]-b[1]) / (a[0]-b[0])

def solution(dots):
    if func(dots[0], dots[1]) == func(dots[2], dots[3]) : return 1
    if func(dots[0], dots[2]) == func(dots[1], dots[3]) : return 1
    if func(dots[0], dots[3]) == func(dots[1], dots[2]) : return 1
    return 0