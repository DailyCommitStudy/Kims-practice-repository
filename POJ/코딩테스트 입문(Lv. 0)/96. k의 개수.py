# i ~ j까지의 수를 가진 리스트의 각 값을 문자열로 바꾸고 ''를 간격으로 하나의 문자열로 만든다.
# 그 문자열에 대해 count 함수를 활용해 k가 몇 개인지 센다.

def solution(i, j, k):
    return ''.join(map(str, range(i, j + 1))).count(str(k))