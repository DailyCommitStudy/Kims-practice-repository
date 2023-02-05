for _ in range(int(input())) :
    s = input()
    if ord(s[0]) < 91: print(s)
    else : print(chr(ord(s[0]) - 32) + s[1:])