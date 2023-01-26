# 자동차 번호의 일의 자리 숫자 = 날짜의 일의 자리 숫자 -> 운행 금지

d = int(input())
print(len(list(filter(lambda x: x==d, map(int, input().split())))))