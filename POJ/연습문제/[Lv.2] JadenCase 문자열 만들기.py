# 단순하게 ' '으로 스플릿하고 첫 알파벳을 대문자로 하면 됨
# s -> ' '로 split -> 각 c가 0번째가 인덱스만 upper()
def solution(s):
    return ' '.join(map(lambda x: ''.join([a.lower() if i else a.upper() for i, a in enumerate(x)]), s.split(' ')))

## 다른 사람 코드
# 현재 문제 조건에는 맞지 않지만.. 이런 .. 함수가 있었다니,... ㄷㄷ
def Jaden_Case(s):
    # 함수를 완성하세요
    return s.title()