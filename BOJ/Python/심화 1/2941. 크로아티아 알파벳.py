# 크로아티아 알파벳을 특수기호로 매핑 후, 문자열의 길이가 정답

str = input()

# 크로아티아 알파벳 replace
for s in ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]:
    str = str.replace(s, ".")

print(len(str))