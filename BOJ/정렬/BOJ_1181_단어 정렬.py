## 828ms

# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순으로

# 숏코딩 형태로 짰지만 나중에는 내가 직접 정렬 알고리즘을 구현해보는 것도 좋겠다.

case = list(set([input() for _ in range(int(input()))]))
case.sort(key=lambda x: (len(x), x))

for c in case:
    print(c)