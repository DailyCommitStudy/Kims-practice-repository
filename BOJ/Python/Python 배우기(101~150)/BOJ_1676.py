def Factorial(n) :
    if n == 0 : return 0
    elif n == 1 : return 1
    return n * Factorial(n-1)

fac = str(Factorial(int(input())))

res = 0
for f in fac[::-1] :
    if f == '0' : res += 1
    else : break
print(res, fac)