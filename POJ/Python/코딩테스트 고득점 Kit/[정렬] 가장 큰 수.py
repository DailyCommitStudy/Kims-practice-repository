# 가장 첫번째 자리 숫자가 큰 순서대로 정렬해야 함 -> 전부 str로 바꿔 정렬 후 붙이고 int로
# [3, 30, 34, 5, 9] -> 9534330
# 3, 30, 34를 34, 3, 30 순으로 정렬해야함 -> 어떻게?

def solution(numbers):
    return "".join(sorted(map(str, numbers), reverse=True))