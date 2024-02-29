# 작은 범위에서 넓혀나가야.. 즉 1R부터 봐야한다.
# 흠........~ 모르겠는데요?

import math
def solution(n,a,b):
    for i in range(1, int(math.log2(n))+1):
        if (a <= n//(2**i) and b <= n//(2**i)) or a > n//(2**i) and b > n//(2**i):
            return i+1