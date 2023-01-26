# 처음 맞는 것 -> 1점
# 연속인 경우 -> 1 + 2 + 3 + .. K

n = int(input())
s = 0
for c in ''.join(input().split(' ')).split('0') : s += sum(range(1, len(c)+1))
print(s)