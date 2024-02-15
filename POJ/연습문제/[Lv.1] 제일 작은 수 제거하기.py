# arr에서 가장 작은 수만 삭제되어야 한다.

def solution(arr):
    arr.remove(min(arr))
    return arr or [-1]