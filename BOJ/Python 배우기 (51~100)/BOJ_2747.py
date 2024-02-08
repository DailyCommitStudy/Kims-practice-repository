a = 1
b = 1
c = 0

for i in range(1, int(input())+1) :
    if i in [1, 2] : c = a
    else :
        c = a + b
        a = b
        b = c

print(c)