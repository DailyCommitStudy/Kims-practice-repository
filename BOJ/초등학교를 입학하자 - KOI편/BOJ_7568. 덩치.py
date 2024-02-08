### x kg, y cm
# (x, y) (p, q)
# x > p, y > q A가 큼
# x > p, y < q or x < p, y > q -> ?
# 나보다 덩치 큰 사람 k명 -> k+1등

## 진짜 단순하게 풀기
# 각 사람별로 돌아가면서 몸무게, 키 비교 -> 크면 count + 1

case = [list(map(int, input().split())) for _ in range(int(input()))]

for c in case:
    cnt = 1
    for i in case:
        if c[0] < i[0] and c[1] < i[1]:
            cnt += 1
    print(cnt)