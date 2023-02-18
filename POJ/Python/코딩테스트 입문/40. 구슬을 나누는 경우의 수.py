def solution(numbers, direction):
    if direction == "right" : return [numbers[-1]] + numbers[:-1]
    else : return numbers[1:] + [numbers[0]]


# 다른 사람 풀이
def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]