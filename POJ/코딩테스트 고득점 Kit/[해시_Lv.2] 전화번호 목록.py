# 접두어 있으면 false, 아니면 true
# 무작정 in 이런 거면 안되고 맨 처음부터 시작하는 그런 접두어야만 함
# 슬라이싱으로 비교 -> 시간 초과
# phone_book[i]로 split을 했을 때 ... 첫 번째 원소가 '' 이면 접두어다! -> 시간이 전보다는 더 빨라졌지만.. 그래도.. 시간 초과
# phone_book[i]를 다른 변수로 저장하고 in으로 비교하는 걸 and로 하면 더 빠르지 않을까? -> 시간 초과

# 음..^^ 반복문 중첩이 문제인가? ㅎㅎ
# 한 번만 순회해서 문제를 해결할 수 있는 방법이 있을까?

def solution(phone_book):
    phone_book.sort(key=len)  # 보다 빠른 탐색을 위한 오름차순 정렬

    for i in range(len(phone_book)):
        a = phone_book[i]
        for j in phone_book[i + 1:]:
            if a in j and j.split(a)[0] == '':
                return False

    return True