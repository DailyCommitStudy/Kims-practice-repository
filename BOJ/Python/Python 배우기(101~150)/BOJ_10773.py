## sys를 안 쓰면 뭔 80ms...............

import sys

case = [0]
for i in range(int(input())) :
    a = int(sys.stdin.readline())
    if a == 0 : case.pop()
    else : case.append(a)
print(sum(case))

