case = [sum(map(int, input().split())) for _ in range(5)]
print(case.index(max(case))+1, max(case))