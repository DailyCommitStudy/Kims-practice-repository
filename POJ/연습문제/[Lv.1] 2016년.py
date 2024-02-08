# 2016년의 몇번째 날인지 구한다
# 7로 나눠 나머지가 1이면 금 2면 토 3이면 일 ... 6이면 수 0이면 목
# 몇 번째 날인지 구하는 방식이 너무 코드를 활용하지 않았나 하는 아쉬움..

m = {1:0, 2:31, 3:60, 4:91, 5:121, 6:152,
     7:182, 8:213, 9:244, 10:274, 11:305, 12:335}
d = ['THU', 'FRI', 'SAT', 'SUN', 'MON',
     'TUE', 'WED']

def solution(a, b):
    return d[(m[a]+b)%7]

# 다른 사람 코드(1)
# 나와 비슷한 느낌.. 코드 내 계산은 더 많지만 더 보기 좋은 것 같다
def getDayName(a,b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return day[(sum(month[:a-1])+b-1)%7]

# 다른 사람 코드(2)
# 라이브러리를 보기좋게 활용한 느낌
# 거기다 날짜를 그냥 문자열로 가져오고 split()한 것도 인상깊다 (왜그랬을까..)
# 2016년 a월 b일을 datetime으로 정의하고, weekday()를 통해 무슨 요일인지 가져온다
# 이때 weekday()는 숫자를 리턴하는데, 0(월요일)부터 6(일요일)을 리턴하기 때문에 인덱싱하기에 좋은 것 같다.
#
import datetime

def getDayName(a,b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    return t[datetime.datetime(2016, a, b).weekday()]

