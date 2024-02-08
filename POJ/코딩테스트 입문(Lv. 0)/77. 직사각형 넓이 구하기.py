# def solution(dots):
#     dots.sort(key=lambda x: (x[0], x[1]))
#     return (dots[2][0]-dots[0][0])*(dots[1][1]-dots[0][1])

## 이게 되네..?
def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])

dots = [[1, 1], [2, 1], [2, 2], [1, 2]]
print(min(dots))
# print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))