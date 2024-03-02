# 요금제 회원제 -> 10일간 자격 부여 할인 제품은 하루에 하나씩만 구매 가능
# 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치할 경우
# 시작일부터 열흘간 판매하는 제품 countdict 만들기
# 한동안 막혀있다가 for 조건에 + 1 해주고 광명 찾다..



def solution(want, number, discount):
    answer = 0

    # 원하는 품목과 개수 딕셔너리로 저장
    want_cnt = {k: v for k, v in zip(want, number)}

    for start in range(len(discount) - 10 + 1):
        # 열흘간 판매할 물건명과 개수 딕셔너리로 카운트
        discount_cnt = {}
        for i in discount[start:start + 10]:
            discount_cnt[i] = discount_cnt.get(i, 0) + 1

        # 같은지 비교 -> 맞으면 return 아니면 계속 반복
        if discount_cnt == want_cnt:
            answer += 1

    return answer

print(solution(	["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))