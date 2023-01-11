X, Y = list(), list()

for _ in range(3) :
    x, y = map(int, input().split())
    X.append(x), Y.append(y)

X, Y = sorted(X), sorted(Y)

if X.count(X[0]) == 1 : print(X[0], end=' ')
else : print(X[-1], end=' ')

if Y.count(Y[0]) == 1 : print(Y[0])
else : print(Y[-1])