# A B C -> 2
# D E  F -> 3 ...
# 문자열을 기준으로 어떤 숫자인지 구하고 그 숫자 + 1 하면 된다
# 문자열을 어떤 숫자인지 어떻게 구하는가? 아스키 코드로 변환해서 3으로 나눈다?
# 1 ~ 27
# (0) 0 1 2 / (1) 3 4 5 / ... + 3 하면 시간

s = input()
res = 0
for c in s:
    tmp = ord(c)-65
    if tmp < 15:
        res += (tmp)//3 + 3
    elif 14 < tmp < 19:
        res += 8
    elif tmp < 22:
        res += 9
    else:
        res += 10
print(res)

# for i in range(26):
#     print(f"{i}, {chr(i+65)}")