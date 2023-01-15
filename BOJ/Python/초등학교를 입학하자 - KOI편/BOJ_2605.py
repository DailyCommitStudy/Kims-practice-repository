# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4
# ...
# 0 1 2 ...

# 0번 -> 그대로, n번(n>0) -> n번 앞으로
N = int(input())
ran = list(map(int, input().split()))
res = list()

for i in range(1, N+1) :
    if ran[i-1] == 0 : res.append(i)
    else : res.insert(i-ran[i-1]-1, i)

for v in res : print(v, end=' ')

