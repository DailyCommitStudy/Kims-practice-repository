# EOF 문제라고 하는 듯..
# 입력이 끝날 때까지 출력
# EOF: End of File. 보통 예외처리를 이용해 처리하는 듯..

import sys

for i in range(100):
    try:
        sys.stdout.write(sys.stdin.readline())
    except:
        break