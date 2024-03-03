# 특정 프로세스가 몇번째로 실행되는가
# 대기중인 프로세스를 하나 꺼내지만, 우선순위가 더 높은 게 있다면 방금 꺼낸 걸 다시 넣음
# 만약 우선순위 높은 게 중간ㅇ ㅔ있으면 그걸 걍 pop하는 거겟지...?
# 그냥 pop말고 head, rear 인덱스 위치를 지정하는 게 좋을듯
# 다시 나갈 수도 있으니 while
# 아.. 최대가 중간에 있으면 앞에 있는 애들 모두 pop, append 후 pop하는 거구나

def solution(priorities, location):
    idx = list(range(len(priorities)))
    ans = 0

    while len(priorities) > 1:  # queue가 빌 때까지
        if max(priorities) > priorities[0]:  # 더 큰 우선순위가 있는 경우 최대값을 앞으로 밀어주기

            while max(priorities) != priorities[0]:  # 인덱스 0에 최대값이 오도록
                priorities.append(priorities.pop(0))  # pop하고 다시 큐에 넣기
                idx.append(idx.pop(0))

            print(priorities)

        priorities.pop(0)
        i = idx.pop(0)

        ans += 1  # 횟수 count

        if i == location:  # location 값이 pop된 경우
            return ans

    return ans + 1

# 오예 !

## 다른 사람 코드
# any..?
# any() 하나라도 True인 게 있으면 True
# all() 모두 True여야 True
# or, and 연산 같군.. 똒똒하드앙
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer