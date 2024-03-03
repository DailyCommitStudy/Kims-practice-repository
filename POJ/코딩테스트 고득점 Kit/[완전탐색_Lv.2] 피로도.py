# 최소 피로도 / 소모 피로도
# 최대한 많이 탐험 -> 다양한 던전 (던전은 하루에 한 번씩 탐험 가능)
# 많ㅇ ㅣ탐험하기 위한 조건
# 1. 최소 피로도가 높은 순대로 탐험을 다니는 것? <-- 일단 이대로 해보기
# 2. 소모 피로도가 낮은 순대로 탐험?
# 하..뭔가 쉽게 생각하면 안될 것 같은데
# 던전은 1 ~ 8개


def solution(k, dungeons):
    # 최소 피로도와 소모 피로도 차이가 높은 순으로 탐험
    dungeons.sort(key=lambda x: (x[0] - x[1]), reverse=True)

    cnt = 0
    for a, b in dungeons:
        print(a, b, k, cnt)
        if a <= k:
            print(1)
            k -= b
            cnt += 1
        else:
            break

    return cnt


# 아니면 규칙을 찾아보는 게 아니라.. 모두 탐색을 해본다?
# 8개 던전을 돌아보는 것은 어떻게 구현할 수 있을까?
# 8중..반복문?

# dfs로 풀어야 하나본데여.. dfs.. 몰라요... 배우긴 했었는데 기억이 안 나는데요..
# 아래 코드를 하면 다.. 탐색을.. 한다더라?
# 아.. 공부를 더 해야겠다..
def solution(k, dungeons):
    answer = -1

    def bt(c, k, ds):
        nonlocal answer

        for i, d in enumerate(ds):
            print(k, d, answer)
            if k >= d[0]:
                new_dungeons = ds.copy()
                new_dungeons.pop(i)

                clear = bt(c + 1, k - d[1], new_dungeons)
                if answer < clear:
                    answer = clear

        return c

    bt(0, k, dungeons)

    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))