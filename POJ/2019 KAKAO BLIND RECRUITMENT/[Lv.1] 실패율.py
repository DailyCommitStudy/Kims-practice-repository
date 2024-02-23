# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 그 비율을 dict로 구하자 아니면 2차원으로
# 1 스테이지일 때, 2 이상이면 클리어한 것

# 2차원 배열로..
# 각 스테이지별로 n 개수 / n 이상인 것 개수

# 미리 stages 정렬 후 슬라이싱을 이용해 실패율을 구하는 방식
def solution(N, stages):
    stages.sort()

    fail = []
    for i in range(1, N + 1):
        if i not in set(stages): # 도달 후 모두 클리어했다, 실패율 0
            fail.append([i, 0])
        else: # i 스테이지에 머무르고 있는 플레이어 존재, 실패율 계산
            rate = stages.count(i) / len(stages[stages.index(i):])
            fail.append([i, rate])

    fail.sort(key=lambda x: x[1], reverse=True)

    return [arr[0] for arr in fail]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

# 다른 방식으로 구해볼까?
# 사전에 count하기! 효율성이 좋아질듯
# 역시 빠르다 굿~

def solution(N, stages):
    rate = []
    a = [0] * (N + 2)

    for s in stages:
        a[s] += 1

    for i in range(1, N + 1):
        if a[i] == 0:
            rate.append([i, 0])
        else:
            rate.append([i, a[i] / sum(a[i:])])

    rate.sort(key=lambda x: x[1], reverse=True)

    return [arr[0] for arr in rate]