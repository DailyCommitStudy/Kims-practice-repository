# 약수면 factor, 배수면 multiple, 둘 다 아니면 neither

while True :
    a, b = map(int, input().split())
    if a + b == 0 : break

    if b%a == 0 : print("factor")
    elif a%b == 0 : print("multiple")
    else : print("neither")