def Rev(s) :
    s = list(s)
    s.reverse()
    return int(''.join(s))

a, b = input().split(' ')
print(Rev(str(Rev(a) + Rev(b))))