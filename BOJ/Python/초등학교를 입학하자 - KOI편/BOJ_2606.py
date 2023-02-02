## 찾아본 반례 다 맞는데 왜.. 안 풀리지............. ㅜㅜ
# a: 감염된 애들(1과 같은 쌍이거나 감염된 애들과 같은 쌍인 경우 add)
# 연결된 애들 연결고리를 만들고, 반복문을 다시 돌면서 판단

# 컴퓨터별로 연결된 애들을 모두 set으로 만들어두고(리스트) 마지막에 1과 연결된 애들을 set으로 합치고 len.

# case = list()
# v = {1}
# N = int(input())
# for i in range(int(input())) :
#     case.append(list(map(int, input().split(' '))))
#     if case[i][0] in v : v.add(case[i][1])
#     elif case[i][1] in v : v.add(case[i][0])
#
# for c in range(len(case)-1, -1, -1) :
#     if case[c][0] in v : v.add(case[c][1])
#     elif case[c][1] in v : v.add(case[c][0])
#
#
# print(len(v)-1)

##
# N = int(input())
# case = {i:set() for i in range(1,N+1)}
# for i in range(int(input())) :
#     a, b = map(int, input().split())
#     case[a].add(b)
#     case[b].add(a)
#
# res = case[1].copy()
# for v in case.values() :
#     if 1 in v : res.update(v)
#
# print(len(res)-1)