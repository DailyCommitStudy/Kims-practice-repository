aS, bS = 100, 100
for _ in range(int(input())) :
    a, b = map(int, input().split())
    if a < b : aS -= b
    elif a > b : bS -= a

print(aS)
print(bS)
