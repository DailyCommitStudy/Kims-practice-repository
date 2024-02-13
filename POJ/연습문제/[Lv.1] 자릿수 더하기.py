'''
각 자릿수를 더해야 하므로 복잡하게 생각할 것 없이 바로
str 후 list로 만들면 각 문자, 캐릭터가 하나씩 원소로 분리되어 저장되므로
이를 활용했다
'''

def solution(n):
    return sum(map(int, str(n)))

# 다른 사람의 코드
# 이게 진짜 코테..를 쓰는 것ㅇ ㅣ아닐까 싶은 느낌
# 난 그냥 기본 랑비르ㅓㄹ리를 활용했는데 진짜 알고리즘을 공부하는 목적에서는
# 이렇게 하는 것이 맞는 듯. ㄷㄷ
def sum_digit(number):
    '''number의 각 자릿수를 더해서 return하세요'''
    if number < 10:
        return number

    return number%10 + sum_digit(number//10)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));