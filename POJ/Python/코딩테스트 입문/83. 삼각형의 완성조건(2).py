def solution(sides):
    # 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 한다
    # 1. 가장 긴 변일 경우
    # 2. 나머지 한 변일 경우
    # 1, 2 -> 1) 2 / 2) x
    # 3, 6 (9) -> 1) 6, 7, 8 / 2) 1, 2, 3, 4
    answer = list(range(min(sides), sum(sides)))

    return answer