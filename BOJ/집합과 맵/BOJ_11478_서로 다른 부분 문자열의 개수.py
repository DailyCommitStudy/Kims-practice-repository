# 문자열 길이 (각 알파벳) = n (5)
# + 2개 연속 = n-1 = n-(2-1) (4)
# + 3개 연속 = n-2 = n-(3-1) (3)
# + 4개 연속 = n-3 = n-(4-1)... (2)
# + n개 연속 = n-(n-1) = 1 (1)
# => n*(n+1)/2
# 근데 서로 다른 것의 개수를 세야하기 때문에 단순 수식으로 하면 안된다.
# 직접 슬라이싱해서 넣어야 하나..

# 240844KB 572ms

import sys

s = sys.stdin.readline().rstrip()
res = set()
for i in range(1, len(s)+1): # 1, 2, 3, 4, 5 (부분 문자열의 길이)
    for j in range(len(s)-i+1): # 슬라이싱할 인덱스
        res.add(s[j:j+i])

sys.stdout.write(f"{len(res)}\n")