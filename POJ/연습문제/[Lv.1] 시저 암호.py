# 핵심은 z에서 a로 넘어가는 것
# z가 25면 26은 0이 되어야 하는 것

# 대, 소문자 모두 있기 때문에 모두에게 적용이 가능한 일반적이어야함
# 밀었을 때 z를 넘어가더라도 정확히 나와야 한다..
# c + n을 한 뒤 a를 뺴고 26으로 나눈 나머지를 a에 더한다.

def solution(s, n):
    answer = ''
    for c in s:
        if c == " ": answer += c
        elif ord(c) >= 97: # 소문자 (97 ~ 122)
                answer += chr((ord(c)+n-ord("a"))%26+ord("a"))
        else: # 대문자 (65 ~)
                answer += chr((ord(c)+n-ord("A"))%26+ord("A"))
    return answer

# 다음에 드는 코드는 아님... 너무 조잡해 보이는데 ㅠㅠ 아닌가?

## 다른 사람의 코드
# 나와 비슷하지만 isupper(), islower()라는 함수를 사용하고
# 리스트로 한 것이 인상적
'''
함수를 사용해 대소판별을 하면서 굳이 공백인지 아닌지유무를
판단할 필요가 없어졌다는 점이 인상적!
'''
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)