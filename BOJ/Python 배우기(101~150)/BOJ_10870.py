a, b, c = 1, 1, 0

for i in range(1, int(input())+1) :
    if i in [1, 2] : c = a
    else :
        c = a + b
        a = b
        b = c

print(c)