# 갈색은 무조건 노란색 격자를 테두리처럼 두른 상태가 된다.
# 노란색 격자의 크기는 yellow의 약수 조합이 될 것..
# yellow 조합이 i * j 라면 i*2 + (j-2)*2 가 brown인지 비교하면 되는 것이 아닐까

def solution(brown, yellow):
    for n in range(1, yellow + 1):
        if yellow % n == 0:  # 약수
            a = yellow // n
            b = yellow // a

            if a * 2 + (b + 2) * 2 == brown:
                return [a + 2, b + 2]

## 다른 사람 코드?
# 아직 공부 X
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]