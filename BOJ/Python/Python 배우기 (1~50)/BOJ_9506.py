n = int(input())
a = list()

while n != -1 :
    for i in range(1, n) :
        if n%i==0 : a.append(i)

    if sum(a) == n :
        print(n, "=", end='')
        for v in a[:-1] :
            print("", v, "+", end='')
        print("", a[-1])
    else :
        print(n, "is NOT perfect.")
    a.clear()

    n = int(input())