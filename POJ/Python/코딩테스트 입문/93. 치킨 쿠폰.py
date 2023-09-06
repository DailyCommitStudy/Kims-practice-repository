# chicken // 10, 그 결과 + 잔여 쿠폰 // 10,... 반복

def solution(chicken):
    answer = 0

    while chicken >= 10:
        # chicken = 쿠폰 수, answer = 서비스 치킨 수
        answer += chicken // 10
        chicken = chicken % 10 + chicken // 10

    return answer

    ## 다른 사람 코드(미친천재들 와 ㅏㅏㅏㅏ)
    # return int(chicken*0.11111111111)
    # answer = (max(chicken,1)-1)//9
    # return answer