# 2개 ~ n//2개
# 1개 틀림.. 뭘까?
# n//2개 이상을 더해야 나오는 수..?

# 효율성을.. 어떻게 챙길 수 있으려나?
# 등차수열의 합 공식..?

def solution(n):
    answer = 1 # 본인
    for i in range(2, n+1): # 2개부터 n//2개까지
        for j in range(1, n//i+1): # 인덱스 1부터 n-i까지
            if sum(range(j, j+i)) == n:
                answer += 1
                break
    return answer


## 다른 사람의 코드
# 나랑 푸는 관점 자체가 달랐네......
# 난 연속되는 숫자의 '개수'에 집착하느라 제대로 풀지 못한듯
# 하 빡쳐 미친것..
def solution(n):
    answer = 1 # 본인

    # 1부터 n까지. 이건 개수가 아니라 i부터 셀 것이라는 듯
    for i in range(1, n//2+1):
        total = 0

        while total < n:
            total += i

            if total == n:
                answer += 1
                break

            i += 1

    return answer

## 다른 사람의 코드2
# 뭐지 시ㅏㄹ..수학과를 가얗ㅅ나보다 내가..
def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])