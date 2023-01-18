## 찾아본 반례 다 맞는데 왜.. 안 풀리지............. ㅜㅜ
# a: 감염된 애들(1과 같은 쌍이거나 감염된 애들과 같은 쌍인 경우 add)
# 연결된 애들 연결고리를 만들고, 반복문을 다시 돌면서 판단

case = list()
v = {1}
N = int(input())
for i in range(int(input())) :
    case.append(list(map(int, input().split(' '))))
    if case[i][0] in v : v.add(case[i][1])
    elif case[i][1] in v : v.add(case[i][0])

for c in range(len(case)-1, -1, -1) :
    if case[c][0] in v : v.add(case[c][1])
    elif case[c][1] in v : v.add(case[c][0])


print(len(v)-1)

