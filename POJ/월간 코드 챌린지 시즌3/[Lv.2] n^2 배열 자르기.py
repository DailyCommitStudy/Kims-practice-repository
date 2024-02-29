# 시간 초과 문제.. -> 모든 matix을 만들지 말고 딱 left부터 right까지 맞는 부분만
# 만들 수 있도록 수정해야할듯

def solution(n, left, right):
    matrix = []
    for i in range(n):
        sub = [0]*n
        for j in range(n):
            sub[j] = max(i+1, j+1)

        matrix += sub

    return matrix[left:right+1]

print(solution(3, 2, 5))