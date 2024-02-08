def solution(order):
    return len([1 for i in str(order) if int(i) in [3, 6, 9]])