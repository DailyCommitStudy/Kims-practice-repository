# 첫 번째 시도에서는 input(), print() 를 사용했고 시간초과라는 결과
# 두 번째 시도에서는 sys를 이용해 입출력 모두 바꿔주었는데 208ms라는 아주 빠른 속도를 보여주었다!!
# 파이썬의 기본 입출력이 시간을 많이 잡아먹는구나 를 체감했다..

import sys

N, M = map(int, sys.stdin.readline().split())

# 도감 입력 (no, 이름 모두에 대해 양쪽에서 매칭시킬 수 있어야하기 때문에 아래처럼 value : key 도 저장
dic = dict()
for i in map(str, range(1, N+1)):
    name = sys.stdin.readline().rstrip()
    dic[i] = name
    dic[name] = i

for i in range(M):
    sys.stdout.write(dic[sys.stdin.readline().rstrip()]+'\n')