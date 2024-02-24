# 1~45 중 6개
# 0이 다 맞거나 다 틀리거나

def solution(lottos, win_nums):
    unknown = lottos.count(0)  # 모르는 값 개수
    matching = len(set(lottos) & set(win_nums))  # 교집합 (서로 매칭되는 번호)

    cnt = [matching + unknown, matching]  # 최대, 최소로 맞춘 개수

    # 순위 계산
    return [7 - i if i > 1 else 6 for i in cnt]

## 다른 사람 코드
# ㄷㄷ 대박
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]