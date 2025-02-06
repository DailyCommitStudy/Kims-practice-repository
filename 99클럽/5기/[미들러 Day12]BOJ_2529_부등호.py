'''
부등호 기호 앞뒤로 넣을 수 있는 숫자는 0 ~ 9까지의 정수
선택된 숫자는 모두 달라야 한다!!

k: 부등호 문자의 개수(2<=k<=9)
(k=9)< < < > < < > < > 
-> 3 < 4 < 5 < 6 > 1 < 2 < 8 > 7 < 9 > 0 -> 3456128790
-> 5 < 6 < 8 < 9 > 0 < 2 < 3 > 1 < 7 > 4 -> 5689023174

부등호를 만족시키는 (k+1) 자리의 정수 중에서 최댓값과 최솟값을 찾아야 한다.

첫 숫자가 9인 경우부터 작아지는 순서대로 모든 경우의 수로 최댓값 탐색
첫 숫자가 0인 경우부터 작아지는 순서대로 모든 경우의 수로 최솟값 탐색

eval()

첫 자리가 0인 경우도 반드시 포함.. 즉, 문자열로 출력해야 함.

아니 숫자를 어떻게 매칭시켜야할지 몰겟음 ㅠㅠㅠ
결국 결과는 정수다.. 라는 걸 기반으로 생각?
k=9라면... 정수는 무조건 10자리 숫자!
0123456789 ~ 9876543210 중에 있다.
k값이 주어지는 순간 정수의 범위도 정해지는 것..
만약, k=3이라면 정수는 4자리 숫자
0123 ~ 9876,,

애초에 근본적으로 자릿수가 제한되어있을 때, 어떻게 서로 다른 숫자로 정수를 구성할 수 있을까?
숫자 조합 탐색??? 어떻게???

chatGPT의 도움..
1. 순열 -> itertools.permutations(0~9, k+1) 함수 활용
2. 백트래킹(DFS 방식) -> 이건 그래프 공부한 뒤... 시도 고고

'''
import itertools

k = int(input())
signs = " " + input().strip() + " "
format_signs = signs.replace(" ", "{}") # 추후 포매팅하기 위해 형식 변경

# 가능한 모든 경우
cases = list(itertools.permutations(range(10), k+1))

# 최댓값 탐색
for case in cases[::-1]:
    if eval(format_signs.format(*case)): # 부등호에 잘 맞아떨어질 경우
        print(''.join(map(str, case)))
        break

# 최솟값 탐색
for case in cases:
    if eval(format_signs.format(*case)): # 부등호에 잘 맞아떨어질 경우
        print(''.join(map(str, case)))
        break

## 최적화 필요... -> 시간/메모리 부족
'''
1. permutations()로 모든 경우의 수(모든 순열)를 미리 가져오는 것은 비효율 (메모리 초과 문제 발생) 
    ex) k = 9일 경우, 10P10 = 10! = 3,628,800 개의 튜플을 한꺼번에 메모리에 저장
    -> 반복문에 직접 사용
    -> 최댓값, 최솟값 한 번에 찾도록
2. 문자열을 코드로 변환하여 실행하는 eval() 대신 부등호 검사를 직접 수행하는 함수 사용
'''

import itertools

k = int(input())
signs = input().strip().split()

# 부등호 관계 검사
def check(nums):
    for i in range(k): # 부등호 위반 여부 판단
        if signs[i] == "<" and nums[i] >= nums[i+1]:
            return False
        if signs[i] == ">" and nums[i] <= nums[i+1]:
            return False
    
    return True  # 모든 조건 만족

max_ans, min_ans = None, None

for perm in itertools.permutations(range(10), k+1):
    if check(perm): # 부등호 관계 만족 여부 체크
        num_str = ''.join(map(str, perm))
        if min_ans is None:
            min_ans = num_str
        max_ans = num_str

print(max_ans)
print(min_ans)