# ROT13: 알파벳을 13글자씩 밀어서 암호화
# 1. 알파벳 배열을 만들고 인덱싱으로? > 44ms


# upp = [chr(i) for i in range(65, 91)]
# low = [chr(i) for i in range(97, 123)]
#
# s = input()
# res = ''
# for c in s :
#     # print(c, ord(c), res)
#     if 65 <= ord(c) <= 90 : # 대문자
#         res += upp[(ord(c)-52)%26]   # -65+13 = -52
#     elif 97 <= ord(c) <= 123 : # 대문자
#         res += low[(ord(c)-97+13)%26] # -97+13 = -84
#     else : res += c
#
# print(res)

# 2. 유니코드 이용? > 44ms

s = input()
res = ''
for c in s :
    if 65 <= ord(c) <= 90 : # 대문자
        res += chr((ord(c)-52)%26+65)
    elif 97 <= ord(c) <= 123 : # 대문자
        res += chr((ord(c)-84)%26+97)
    else : res += c

print(res)