V = int(input())
case = input()

if case.count('A') ==  case.count('B') : print('Tie')
elif case.count('A') > case.count('B')  : print('A')
else : print('B')