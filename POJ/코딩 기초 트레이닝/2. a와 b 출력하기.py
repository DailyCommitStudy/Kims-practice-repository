a, b = map(int,input().split())
print(f'a = {a}\nb = {b}')

# 문자열을 split() 하는 과정에서 문자열에 좌우 공백이 있을 경우를 고려하여, strip()을 추가하는 것이 보다 좋은 코드인 것 같다.
'''
a, b = map(int,input().strip().split())
print(f'a = {a}\nb = {b}')
'''