# 두 변의 길이으 ㅣ합이 가장 긴 변보다 작아야 함.
# 즉, 1 4일 경우 4일 수밖에 없음.
# 즉, 4 6일 경우 긴 게 x면 6 7 8 9. 긴 게 6이면 3, 4, 5
# 즉, 3 6일 경우 긴 변이 x면 7, 8. 긴 게 6이면 4, 5, 6
# 즉, 7 11일 경우 긴 변이 x면 12, 13, 14, 15, 16, 17. 긴 게 11이면 5, 6, 7, 8, 9, 10, 11
# 7+x = 12 이상이어야 함. x = 12-7(5)부터 sides[1](11) 까지

def solution(sides):
    sides.sort()

    # 긴 변이 sides[1]
    answer = set(range(sides[1] - sides[0] + 1, sides[1] + 1))
    # 긴 변이 x
    answer.update(set(range(sides[1] + 1, sum(sides))))

    return len(answer)

# 젠장.. 역시 사람은 수학을 잘 해야..
def solution(sides):
    return sum(sides) - max(sides) + min(sides) - 1

def solution(sides):
    return 2 * min(sides) - 1