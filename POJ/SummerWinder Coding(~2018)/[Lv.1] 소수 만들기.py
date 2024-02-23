# nums에 들어있는 숫자 중 가장 큰 3개를 더해 상한선 구하기 -> 체로 소수 여부 구해두기
# nums 속 3개씩 구해서 체 안에 있는지 아닌지 여부 체크
# 문제: nums 속 요소들을 3개씩 어떻게 선택하도록 하는가?
# nums 속 요소를 어떻게 3개씩 순회할 수 있게 하는가?
# 3중 반복문
## 1) i, 0 ~ n-3
## 2) j, j+1 ~ n-2
## 3) k, k+1 ~ n-1

def solution(nums):
    answer = 0
    m = sum(sorted(nums)[-3:])  # 소수 최대 상한선

    # 에라토스테네스의 체로 m까지의 소수가 무엇인지 구한다
    a = [False, False] + [True] * (m - 1)
    for i in range(m + 1):
        if a[i]:
            for j in range(i * 2, m + 1, i):
                a[j] = False

    # nums 중 3개를 합한 것이 소수인가?
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if a[sum([nums[i], nums[j], nums[k]])]:
                    answer += 1

    return answer


# 다른 사람들의 코드(1)
# combinations 함수 활용
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer

# 다른 사람들의 코드(2)
# 나와 거의 유사한 방식인데 s[i*2::i] = [0] * ((n - i)//i) 이 코드가 신기하당
def sieve(n):
    """
    에라토스테네스의 체
    """
    if n < 2:
        return []

    #[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    s = [0, 0] + [1] * (n - 1)

    for i in range(2, int(n**.5)+1):
        if s[i]:
            s[i*2::i] = [0] * ((n - i)//i)
    return [i for i, v in enumerate(s) if v]

def solution(nums):
    primes = sieve(3000)

    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if (nums[i] + nums[j] + nums[k]) in primes:
                    count += 1

    return count
