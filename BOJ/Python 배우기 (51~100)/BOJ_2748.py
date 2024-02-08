# def Fib(n) :
#     if n == 0 : return 0
#     elif n == 1 : return 1
#     else : return Fib(n-1) + Fib(n-2)
#
#
# print(Fib(int(input())))

## 2

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
