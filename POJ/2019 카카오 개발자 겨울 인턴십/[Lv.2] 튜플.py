# 이 문제의 핵심은 1, 1~2, 1~3, ... 같은 식으로 표현한다는 것
# 즉, 가장 긴 것만 가져와서 될 것이 아니라 짧은 애들부터 보면서 완성해야 한다.
# 0번째 -> 0번째 자리 값
# 1번째부터는 앞에 추가한 값들과 중복되지 않는 값을 추가해야됨

def solution(s):
    # 스트링 형태로 된 s를 리스트 형태로 변환
    s = sorted(map(lambda x: list(map(int, x.split(","))), s[2:-2].split("},{")),
               key=len)

    # 순서에 맞는 원래 형태의 튜플 찾기
    answer = []
    for c in s:
        for a in c:  # 중복되지 않는 값을 넣어야함
            if a not in answer:
                answer.append(a)

    return answer