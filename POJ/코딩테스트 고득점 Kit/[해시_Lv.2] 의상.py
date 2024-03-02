# 매일 다른 옷을 조합
# 종류별로 최대 1가지 의상만 착용
# 최소 1개의 의상은 입어야 한다
# 서로 다른 옷의 조합의 수

# 타입 : [아이템] 처럼 딕셔너리로 저장 후, 각 타입별 개수로 경우의 수를 구한다

def solution(clothes):
    case = {}
    # 갖고 있는 아이템 타입별 카운트
    for c, t in clothes:
        case[t] = case.get(t, 0) + 1

    # 타입별 아이템 개수 + 1(안입을 경우) 후 곱하면 경우의 수가 나온다
    answer = 1
    for i in case.values():
        answer *= i + 1

    # 아무것도 안 입는 경우 제외
    return answer - 1

## 나중에 .. 다른 사람 코드 봐야됨
