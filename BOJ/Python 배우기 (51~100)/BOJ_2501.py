#n의 약수들 중 k번째로 작은 수를 출력

n, k = map(int, input().split())

count, m = 0, 0
for i in range(1, n+1) :
    if n%i == 0 :
        count += 1
        if count == k :
            m = i
            break

print(m)