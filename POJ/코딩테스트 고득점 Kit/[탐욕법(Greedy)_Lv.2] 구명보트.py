# 구명보트를 최대한 적게 쓸거면 2명의 합이 최대한 limit에 가까워야 한다는 거잖음?
# 정렬해서 가장 큰 값 + 작은 값 더해보고 limit 안이면 둘 다 pop 후 answer += 1
# 아니면 큰 값만 pop 후 answer += 1
# 첫 시도 정확도 결과는 좋았으나 시간 초과가..^^
# pop말고 다른 걸 써봐야겠구나
# /... 어떻게해야함..?ㅋ

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)

    while people:
        n = len(people)
        answer += 1

        if len(people) == 1:  # 1명만 남은 경우 -> 구조 후 break
            break

        # people 내 최소, 최대 몸무게 합이 limit을 넘지 않을 경우 둘 모두 구조
        if people[0] + people[n - 1] <= limit:
            people = people[1:-1]

        else:  # limit을 넘으면 최대 몸무게만 구조
            people = people[1:]

    return answer

# 이렇게 바꿔도 시간복잡도 문제가 안 사라져서.. 챗지피티한테(ㅋ) 도움을 구햇더니
# 꼭 슬라이싱을 할 필요가 없다는 걸 알았다.

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)

    l, r = 0, len(people) - 1
    while l <= r:
        answer += 1

        if l == r:  # 1명만 남은 경우 -> 구조 후 break
            break

        # people 내 최소, 최대 몸무게 합이 limit을 넘지 않을 경우 둘 모두 구조
        if people[l] + people[r] <= limit:
            r -= 1

        l += 1

    return answer


# 다른 사람 콬드
# 나랑 유사하면서도 둘을 동시에 구조할 때만 answer를 더해 마지막에 사람들의 명 수에서 뺀 것이 인상적
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer