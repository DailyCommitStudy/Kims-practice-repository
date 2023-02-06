#97~122 / 65~90
s = input().upper()
a = [s.count(chr(i)) for i in range(65, 91)]

if a.count(max(a)) > 1 : print('?')
else : print(chr(a.index(max(a))+65))