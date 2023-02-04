# 대 -> 소, 소 -> 대.. 흠 유니코드를 이용해  볼까 ord, shr
# A 65 ~ Z 90 / a 97 ~ z 122
# print(f'A {ord("A")} Z {ord("Z")} a {ord("a")} z  {ord("z")} 122 { chr(122)}')

s = input()
res = ''
for c in s :
    if ord(c) <= 90 : res += chr(ord(c)+32)
    else : res += chr(ord(c)-32)
print(res)