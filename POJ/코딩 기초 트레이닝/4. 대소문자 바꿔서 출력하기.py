str = input()

for s in str:
    if s.upper() == s: # 대문자
        print(s.lower(), end='')
    else: # 소문자
        print(s.upper(), end='')

# 다른 사람 풀이
# 아 억울해...
print(input().swapcase())