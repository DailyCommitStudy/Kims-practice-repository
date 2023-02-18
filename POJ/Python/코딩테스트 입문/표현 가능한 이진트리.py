class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

tree = []

def solution(numbers):
    ans = list()
    for n in numbers:
        case = list(str(bin(n)))[2:]
        print(case)
        flag = True
        for i in range(len(case)):
            if case[i // 2] == '0':
                ans.append(0)
                flag = False
                break
        if flag: ans.append(1)

    return ans

print(solution([42,111]))