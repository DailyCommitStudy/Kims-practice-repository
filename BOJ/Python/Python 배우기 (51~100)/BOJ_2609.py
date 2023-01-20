a, b = sorted(map(int, input().split()))
G = a

for g in range(a, 0, -1) :
    if ((a%g == 0) and (b%g == 0)) :
        G = g
        break

print(G)
print(a*b//G)